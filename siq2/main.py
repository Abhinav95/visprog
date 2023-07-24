import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from functools import partial

from engine.utils import ProgramGenerator, ProgramInterpreter
from prompts.siq2 import create_prompt

import pandas as pd
import webvtt
from tqdm import tqdm

experiment_setting = dict(
    use_subtitles=True,
    use_diarization=False,
    use_video_description=False,
    use_audio_description=True,
    use_timed_subtitles=True,
    use_context=True
    num_programgen_examples=12
)
EXPERIMENT_NAME = (
    "qa"+
    "_sub_"+str(experiment_setting['use_subtitles'])+
    "_dia_"+str(experiment_setting['use_diarization'])+
    "_vid_"+str(experiment_setting['use_video_description'])+
    "_aud_"+str(experiment_setting['use_audio_description'])+
    "_timedsub_"+str(experiment_setting['use_timed_subtitles'])+
    "_context_"+str(experiment_setting['use_context'])+
    "_progexamples_"+str(experiment_setting['num_programgen_examples'])
)

interpreter = ProgramInterpreter(dataset='siq2')

prompter = partial(create_prompt,num_prompts=experiment_setting['num_programgen_examples'],method='random')
generator = ProgramGenerator(prompter=prompter, model='gpt-3.5-turbo')

dataset_dir = "/home/abhinav_shukla_research/bucket/Social-IQ-2.0-Challenge/siq2"

val_json_path = os.path.join(dataset_dir, 'qa/qa_val.json')
val_df = pd.read_json(val_json_path,lines=True)
test_json_path = os.path.join(dataset_dir, 'qa/qa_test.json')
test_df = pd.read_json(test_json_path, lines=True)
transcripts_path = os.path.join(dataset_dir, 'transcript')
videos_path = os.path.join(dataset_dir, 'video')
audios_path = os.path.join(dataset_dir, 'audio/wav')

existing_video_list = os.listdir(videos_path)
existing_audio_list = os.listdir(audios_path)
existing_transcript_list = os.listdir(transcripts_path)

assert(len(existing_audio_list)==len(existing_video_list))
assert(len(existing_audio_list)==len(existing_transcript_list))

def compute_correctness(df):
    correct = 0
    total = 0

    for _,row in tqdm(df.iterrows(),total=len(df), position=0, leave=True):
        if(row['result'] != None and row['result'] != '-1'):
            if(row['answer_idx'] in [int(c) for c in row['result'] if c.isdigit()]):
                correct += 1
            total += 1
    print(total, "valid answers recorded")
    return (1.0 * correct/total)
    
val_df['result'] = [None for _ in range(len(val_df))]
test_df['result'] = [None for _ in range(len(test_df))]
print("Beginning Validation")
running_corrects_val = 0
running_total_val = 0
for i,row in val_df.iterrows():
    try:
        if row['vid_name']+'.vtt' not in existing_transcript_list or row['vid_name']+'.mp4' not in existing_video_list or row['vid_name']+'.wav' not in existing_audio_list:
            print(row['vid_name'],"does not have data files, ignoring")
        else:            
            question = "Question: "+row['q']
            question += "\nOptions:\n" + '0: '+row['a0']+'\n'+ '1: '+row['a1']+'\n'+ '2: '+row['a2']+'\n'+ '3: '+row['a3']
            # prog = "\nPlaceholder\nProgram\nText\n"
            prog,_ = generator.generate(dict(question=question))
            print('\n',question, prog)
            init_state = dict(
                METHOD=dict(
                    use_subtitles=experiment_setting['use_subtitles'],
                    use_diarization=experiment_setting['use_diarization'],
                    use_video_description=experiment_setting['use_video_description'],
                    use_audio_description=experiment_setting['use_audio_description'],
                    use_timed_subtitles=experiment_setting['use_timed_subtitles'],
                    use_context=experiment_setting['use_context']                    
                ),
                DATASET_INFO=dict(
                    dataset_dir=dataset_dir,
                    transcripts_path=transcripts_path,
                    videos_path=videos_path,
                    audios_path=audios_path            
                ),
                VIDEO_ID=row['vid_name'],
                QUESTION=question
            )
            # result = '0'
            result, prog_state = interpreter.execute(prog,init_state,inspect=False)
            val_df.loc[i, 'result'] = result

            if row['answer_idx'] in [int(c) for c in result if c.isdigit()]:
                running_corrects_val += 1
            running_total_val += 1
            print("Question:", question)
            print("Correct answer:", row['answer_idx'], "Given answer:", [int(c) for c in result if c.isdigit()])
            print("[Iteration:",str(i)+'/'+str(len(val_df)-1)+',',"Running validation accuracy:", f"%06.3f" % (100.0 * running_corrects_val/running_total_val)+']')

    except Exception as e:
        print(e)

output_json_path = "qa_val_"+EXPERIMENT_NAME+".json"
print("Validation finished. Exporting json to:", output_json_path)
val_df.to_json(output_json_path, orient='records', lines=True)
validation_accuracy = compute_correctness(val_df)
print("Accuracy:", validation_accuracy)
with open("val_"+EXPERIMENT_NAME+".txt", 'w') as f:
    f.write(str(validation_accuracy)+'\n')


# print("Beginning test")
# running_total_test = 0
# for i,row in test_df.iterrows():
#     try:
#         if row['vid_name']+'.vtt' not in existing_transcript_list or row['vid_name']+'.mp4' not in existing_video_list or row['vid_name']+'.wav' not in existing_audio_list:
#             print(row['vid_name'],"does not have data files, ignoring")
#         else:            
#             question = "Question: "+row['q']
#             question += "\nOptions:\n" + '0: '+row['a0']+'\n'+ '1: '+row['a1']+'\n'+ '2: '+row['a2']+'\n'+ '3: '+row['a3']
#             # prog = "\nPlaceholder\nProgram\nText\n"
#             prog,_ = generator.generate(dict(question=question))
#             print('\n',question, prog)
#             init_state = dict(
#                 METHOD=dict(
#                     use_subtitles=experiment_setting['use_subtitles'],
#                     use_diarization=experiment_setting['use_diarization'],
#                     use_video_description=experiment_setting['use_video_description'],
#                     use_audio_description=experiment_setting['use_audio_description'],
#                     use_timed_subtitles=experiment_setting['use_timed_subtitles']
#                 ),
#                 DATASET_INFO=dict(
#                     dataset_dir=dataset_dir,
#                     transcripts_path=transcripts_path,
#                     videos_path=videos_path,
#                     audios_path=audios_path            
#                 ),
#                 VIDEO_ID=row['vid_name'],
#                 QUESTION=question
#             )
#             # result = '0'
#             result, prog_state = interpreter.execute(prog,init_state,inspect=False)
#             test_df.loc[i, 'result'] = result
#             running_total_test += 1
#             print("[Iteration:",str(i)+'/'+str(len(test_df)-1)+']')

#     except Exception as e:
#         print(e)

# output_json_path = "qa_test_"+EXPERIMENT_NAME+".json"
# print("Inference finished. Exporting json to:", output_json_path)
# test_df.to_json(output_json_path, orient='records', lines=True)
# print("\n\n", EXPERIMENT_NAME)
# print("Total Vald:", str(running_total_val)+'/'+str(len(val_df)))
# print("Total Test:", str(running_total_test)+'/'+str(len(test_df)))
# print("Validation Accuracy:", compute_correctness(val_df))



exit(0)

question = """
Question: Do the men agree with the woman?
Options:
 0: They definitely agree with the woman.
 1: The men nod when the woman completes their sentences because they approve of what she has said.
 2: The men are discussing a completely different topic.
 3: No, they do agree with the woman.
"""
prog,_ = generator.generate(dict(question=question))
print(prog)

init_state = dict(
    METHOD=dict(
        use_subtitles=experiment_setting['use_subtitles'],
        use_diarization=experiment_setting['use_diarization'],
        use_video_description=experiment_setting['use_video_description'],
        use_audio_description=experiment_setting['use_audio_description'],
        use_timed_subtitles=experiment_setting['use_timed_subtitles']
    ),
    DATASET_INFO=dict(
        dataset_dir=dataset_dir,
        transcripts_path=transcripts_path,
        videos_path=videos_path,
        audios_path=audios_path            
    ),
    VIDEO_ID="ZbiGzK3slg0",
    QUESTION=question
)
result, prog_state = interpreter.execute(prog,init_state,inspect=False)
print("Finished exection, answer is:\n", result)

# print(prog_state)