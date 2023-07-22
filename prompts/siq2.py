import random

SIQ2_CURATED_EXAMPLES=[
"""
Question: Why does the man speak for the blonde woman when the curly haired woman asks her a question?
Options:
 0: He speaks for her because he wants to protect her from getting arrested, but he doesn't want to get in trouble himself.
 1: He speaks for her because she is shy.
 2: He speaks for her because he doesn't want her to say anything that could incriminate him
 3: The man is speaking in such a serious tone to the curly haired woman because he wants to emphasize the seriousness of the situation.
Program:
SUBTITLES=GetSubtitles(video=VIDEO_ID)
TIMESTAMP=DescribeVideo(video=VIDEO_ID, timestamp=None, query='At what timestep does the curly haired woman ask the blonde woman a question?')
VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=TIMESTAMP, query='Why does the man speak for the blonde woman?')
FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, timestamp=TIMESTAMP)
RESULT=EvaluateText(text=FINAL_TEXT, query="What is the most likely choice from the given options? Respond in the format 'answer_idx: index of the option, answer_text: text of the option'")
""",
"""
Question: Why does the man in the video laugh when the boy sitting closest to him says "both" in response to his question?
Options:
 0: He thinks it's funny and no one would answer it seriously.
 1: He thinks it is a cute response
 2: He thinks the boy is dumb for not answering his question.
 3: He thinks the girls are too young to be playing in the park.
Program:
SUBTITLES=GetSubtitles(video=VIDEO_ID)
TIMESTAMP=EvaluateText(text=SUBTITLES, query='At what timestamp does the boy say "both"? Return an exact time')
VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=TIMESTAMP, query='Why does the man laugh?')
FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, timestamp=TIMESTAMP)
RESULT=EvaluateText(text=FINAL_TEXT, query="What is the most likely choice from the given options? Respond in the format 'answer_idx: index of the option, answer_text: text of the option'")
""",
"""
Question: Why does the older woman smirk at 0:37?
Options:
 0: She finds it amusing.
 1: She didn't like the answer the woman gave her and is laughing at her.
 2: She did not like the answer she was given.
 3: She is thinking about the answer the woman gave and realizing her point of view.
Program:
SUBTITLES=GetSubtitles(video=VIDEO_ID)
VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=37, query='Why does the woman smirk?')
FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, timestamp=37)
RESULT=EvaluateText(text=FINAL_TEXT, query="What is the most likely choice from the given options? Respond in the format 'answer_idx: index of the option, answer_text: text of the option'")
"""
]

def create_prompt(inputs,num_prompts=3,method='random',seed=42,group=0):
    if method=='all':
        prompt_examples = SIQ2_CURATED_EXAMPLES
    elif method=='random':
        random.seed(seed)
        prompt_examples = random.sample(SIQ2_CURATED_EXAMPLES,num_prompts)
    else:
        raise NotImplementedError

    prompt_examples = '\n'.join(prompt_examples)
    prompt_examples = f'Think step by step to pick the most likely choice from the given options for the question.\n\n{prompt_examples}'


    return prompt_examples + "\nQuestion: {question}\nProgram:".format(**inputs)