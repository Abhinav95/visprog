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

interpreter = ProgramInterpreter(dataset='siq2')

prompter = partial(create_prompt,method='all')
generator = ProgramGenerator(prompter=prompter, model='gpt-3.5-turbo')

dataset_dir = "/home/abhinav_shukla_research/bucket/Social-IQ-2.0-Challenge/siq2"

val_json_path = os.path.join(dataset_dir, 'qa/qa_val.json')
val_df = pd.read_json(val_json_path,lines=True)
transcripts_path = os.path.join(dataset_dir, 'transcript')
videos_path = os.path.join(dataset_dir, 'video')
audios_path = os.path.join(dataset_dir, 'audio/wav')

existing_video_list = os.listdir(videos_path)
existing_audio_list = os.listdir(audios_path)
existing_transcript_list = os.listdir(transcripts_path)

assert(len(existing_audio_list)==len(existing_video_list))
assert(len(existing_audio_list)==len(existing_transcript_list))

# for i,row in val_df.iterrows():
#     try:
#         if row['vid_name']+'.vtt' not in existing_transcript_list or row['vid_name']+'.mp4' not in existing_video_list or row['vid_name']+'.wav' not in existing_audio_list:
#             print(row['vid_name'],"does not have data files, ignoring")
#         else:            
#             # print(i, row)
#             # captions = [caption.text for caption in webvtt.read(os.path.join(transcripts_path, row["vid_name"] + '.vtt'))]
#             # transcript = '\n'.join(captions)
#             question = "Question: "+row['q']
#             question += "\nOptions:\n" + '0: '+row['a0']+'\n'+ '1: '+row['a1']+'\n'+ '2: '+row['a2']+'\n'+ '3: '+row['a3']
#             prog,_ = generator.generate(dict(question=question))
#             print('\n',question, prog)
#     except Exception as e:
#         print(e)
#     if i>50:
#         break

# exit(0)

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
        use_subtitles=True,
        use_diarization=True,
        use_video_description=True,
        use_audio_description=True,
        use_timed_subtitles=True
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

print(prog_state)