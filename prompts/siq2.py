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
VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=None, query=None)
VIDEO_SEARCH_RESULT_1=SearchVideo(video=VIDEO_ID, timestamp=None, query="Is the curly haired woman talking?")
VIDEO_SEARCH_RESULT_2=SearchVideo(video=VIDEO_ID, timestamp=None, query="Is the man talking?")
SEARCH_RESULT_TEXT=ConcatenateText(text1=VIDEO_SEARCH_RESULT_1, text2=VIDEO_SEARCH_RESULT_2)
FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, additional_context=SEARCH_RESULT_TEXT)
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
VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=None, query=None)
VIDEO_SEARCH_RESULT_1=SearchVideo(video=VIDEO_ID, timestamp=None, query="Is the man laughing?")
TEXT_SEARCH_RESULT_1=EvaluateText(text=SUBTITLES, query="When does the boy say 'both'? Summarize any additional context from the subtitles")
SEARCH_RESULT_TEXT=ConcatenateText(text1=VIDEO_SEARCH_RESULT_1, text2=TEXT_SEARCH_RESULT_1)
FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, additional_context=SEARCH_RESULT_TEXT)
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
VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=37, query=None)
VIDEO_SEARCH_RESULT_1=SearchVideo(video=VIDEO_ID, timestamp=37, query="Is the woman amused?")
TEXT_SEARCH_RESULT_1=EvaluateText(text=SUBTITLES, query="Summarize the mood of the text around 0:37")
SEARCH_RESULT_TEXT=ConcatenateText(text1=VIDEO_SEARCH_RESULT_1, text2=TEXT_SEARCH_RESULT_1)
FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, additional_context=SEARCH_RESULT_TEXT)
RESULT=EvaluateText(text=FINAL_TEXT, query="What is the most likely choice from the given options? Respond in the format 'answer_idx: index of the option, answer_text: text of the option'")
""",
"""
Question: Why doesn't the white haired man join in the conversation?
Options:
 0: The white haired man is too busy taking pictures to join in the conversation.
 1: The white haired man doesn't join in the conversation because he doesn't want to be bothered
 2: The white haired man doesn't join in the conversation because he's mute.
 3: The white haired man is deaf and cannot hear the conversation.
Program:
SUBTITLES=GetSubtitles(video=VIDEO_ID)
VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=None, query=None)
VIDEO_SEARCH_RESULT_1=SearchVideo(video=VIDEO_ID, timestamp=None, query="Is the white haired man taking a picture?")
TEXT_SEARCH_RESULT_1=EvaluateText(text=SUBTITLES, query="Summarize this conversation with the knowledge that the white haired man does not join in")
SEARCH_RESULT_TEXT=ConcatenateText(text1=VIDEO_SEARCH_RESULT_1, text2=TEXT_SEARCH_RESULT_1)
FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, additional_context=SEARCH_RESULT_TEXT)
RESULT=EvaluateText(text=FINAL_TEXT, query="What is the most likely choice from the given options? Respond in the format 'answer_idx: index of the option, answer_text: text of the option'")
""",
"""
Question: What is the overall mood of the scene?
Options:
 0: The mood is very delightful
 1: He thinks football is a team-based sport.
 2: The scene is chaotic and messy.
 3: The mood of the scene is serious.
Program:
SUBTITLES=GetSubtitles(video=VIDEO_ID)
VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=None, query=None)
VIDEO_SEARCH_RESULT_1=SearchVideo(video=VIDEO_ID, timestamp=None, query="Describe the mood of this scene")
TEXT_SEARCH_RESULT_1=EvaluateText(text=SUBTITLES, query="Summarize the tone of this conversation")
SEARCH_RESULT_TEXT=ConcatenateText(text1=VIDEO_SEARCH_RESULT_1, text2=TEXT_SEARCH_RESULT_1)
FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, additional_context=SEARCH_RESULT_TEXT)
RESULT=EvaluateText(text=FINAL_TEXT, query="What is the most likely choice from the given options? Respond in the format 'answer_idx: index of the option, answer_text: text of the option'")
""",
"""
Question: What is the atmosphere like between the man and the woman at the beginning of the video?
Options:
 0: passionate and loving at the beginning because they are reminiscing
 1: They were arguing about the weather.
 2: Robbie and the woman seem close and uncomfortable.
 3: The atmosphere is tense and awkward at the beginning because they are miscommunicating
Program:
SUBTITLES=GetSubtitles(video=VIDEO_ID)
VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=None, query=None)
VIDEO_SEARCH_RESULT_1=SearchVideo(video=VIDEO_ID, timestamp=None, query="What is the emotion and mood of the video at the beginning?")
TEXT_SEARCH_RESULT_1=EvaluateText(text=SUBTITLES, query="Summarize the mood at the beginning of the text")
SEARCH_RESULT_TEXT=ConcatenateText(text1=VIDEO_SEARCH_RESULT_1, text2=TEXT_SEARCH_RESULT_1)
FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, additional_context=SEARCH_RESULT_TEXT)
RESULT=EvaluateText(text=FINAL_TEXT, query="What is the most likely choice from the given options? Respond in the format 'answer_idx: index of the option, answer_text: text of the option'")
""",
"""
Question: Why does the man in the light colored shirt smile at 0:05?
Options:
 0: He smiles because he realizes that the man in the brown shirt is teasing him
 1: He smiles because he realizes that the man in the brown shirt is jealous of him
 2: He smiles because he appreciates the man in the brown shirt's sense of humor.
 3: He smiles because he remembers a funny joke.
Program:
SUBTITLES=GetSubtitles(video=VIDEO_ID)
VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=5, query=None)
VIDEO_SEARCH_RESULT_1=SearchVideo(video=VIDEO_ID, timestamp=5, query="Why is the man in the light colored shirt smiling?")
VIDEO_SEARCH_RESULT_2=SearchVideo(video=VIDEO_ID, timestamp=5, query="What is the man in the brown shirt doing?")
TEXT_SEARCH_RESULT_1=EvaluateText(text=SUBTITLES, query="Summarize the tone of this conversation around 0:05")
SEARCH_RESULT_TEXT=ConcatenateText(text1=VIDEO_SEARCH_RESULT_1, text2=VIDEO_SEARCH_RESULT_2, text3=TEXT_SEARCH_RESULT_1)
FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, additional_context=SEARCH_RESULT_TEXT)
RESULT=EvaluateText(text=FINAL_TEXT, query="What is the most likely choice from the given options? Respond in the format 'answer_idx: index of the option, answer_text: text of the option'")
""",
"""
Question: Did the lady on the right appear to enjoy the conversation?
Options:
 0: She is fearful of speaking to the man.
 1: The woman on the right is happy to be a part of the conversation.
 2: The woman on the right is distracted by her phone.
 3: The lady on the right is wondering what to wear.
Program:
SUBTITLES=GetSubtitles(video=VIDEO_ID)
VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=None, query=None)
VIDEO_SEARCH_RESULT_1=SearchVideo(video=VIDEO_ID, timestamp=None, query="Does the lady on the right appear to enjoy the conversation?")
VIDEO_SEARCH_RESULT_2=SearchVideo(video=VIDEO_ID, timestamp=None, query="Is the lady on the right fearful or distracted?")
SEARCH_RESULT_TEXT=ConcatenateText(text1=VIDEO_SEARCH_RESULT_1, text2=VIDEO_SEARCH_RESULT_2)
FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, additional_context=SEARCH_RESULT_TEXT)
RESULT=EvaluateText(text=FINAL_TEXT, query="What is the most likely choice from the given options? Respond in the format 'answer_idx: index of the option, answer_text: text of the option'")
""",
"""
Question: What are the police officers' demeanor like when they talked to the man in the car?
Options:
 0: The police officers' demeanor is professional and inquisitive.
 1: They are stern and unapproachable.
 2: The police officers' demeanor is invested and fascinated.
 3: The police officers are laughing and joking with the men.
Program:
SUBTITLES=GetSubtitles(video=VIDEO_ID)
VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=None, query=None)
VIDEO_SEARCH_RESULT_1=SearchVideo(video=VIDEO_ID, timestamp=None, query="Are the police officers talking to the man in the car?")
VIDEO_SEARCH_RESULT_2=SearchVideo(video=VIDEO_ID, timestamp=None, query="What is the demeanour of the police officers?")
TEXT_SEARCH_RESULT_1=EvaluateText(text=SUBTITLES, query="Summarize the overall tone of the police officers when they talk to the man")
SEARCH_RESULT_TEXT=ConcatenateText(text1=VIDEO_SEARCH_RESULT_1, text2=VIDEO_SEARCH_RESULT_2, text3=TEXT_SEARCH_RESULT_1)
FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, additional_context=SEARCH_RESULT_TEXT)
RESULT=EvaluateText(text=FINAL_TEXT, query="What is the most likely choice from the given options? Respond in the format 'answer_idx: index of the option, answer_text: text of the option'")
""",
 """
Question: Does the woman like the man?
Options:
 0: Yes, she is grateful for something he has done.
 1: Yes, the woman thinks the man is good.
 2: Yes, she thinks the man is nice.
 3: She is fond of him.
Program:
SUBTITLES=GetSubtitles(video=VIDEO_ID)
VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=None, query=None)
VIDEO_SEARCH_RESULT_1=SearchVideo(video=VIDEO_ID, timestamp=None, query="Is the woman comfortable?")
VIDEO_SEARCH_RESULT_2=SearchVideo(video=VIDEO_ID, timestamp=None, query="What is the overall mood of the scene?")
TEXT_SEARCH_RESULT_1=EvaluateText(text=SUBTITLES, query="Summarize the overall tone of the woman when she speaks to the man")
SEARCH_RESULT_TEXT=ConcatenateText(text1=VIDEO_SEARCH_RESULT_1, text2=VIDEO_SEARCH_RESULT_2, text3=TEXT_SEARCH_RESULT_1)
FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, additional_context=SEARCH_RESULT_TEXT)
RESULT=EvaluateText(text=FINAL_TEXT, query="What is the most likely choice from the given options? Respond in the format 'answer_idx: index of the option, answer_text: text of the option'")
""",
"""
Question: How is the man in the back presenting himself?
Options:
 0: He's very talkative and opinionated.
 1: He's silent
 2: He's very involved and engaged
 3: He's wearing a red shirt.
Program:
SUBTITLES=GetSubtitles(video=VIDEO_ID)
VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=None, query=None)
VIDEO_SEARCH_RESULT_1=SearchVideo(video=VIDEO_ID, timestamp=None, query="How does the man in the back look?")
VIDEO_SEARCH_RESULT_2=SearchVideo(video=VIDEO_ID, timestamp=None, query="What is the behaviour of the man in the back?")
TEXT_SEARCH_RESULT_1=EvaluateText(text=SUBTITLES, query="Summarize the overall tone of the conversation")
SEARCH_RESULT_TEXT=ConcatenateText(text1=VIDEO_SEARCH_RESULT_1, text2=VIDEO_SEARCH_RESULT_2, text3=TEXT_SEARCH_RESULT_1)
FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, additional_context=SEARCH_RESULT_TEXT)
RESULT=EvaluateText(text=FINAL_TEXT, query="What is the most likely choice from the given options? Respond in the format 'answer_idx: index of the option, answer_text: text of the option'")
""",
# """
# Question: What is the relationship between the two woman?
# Options:
#  0: The two woman seem to be friends.
#  1: The two woman seem to know each other well.
#  2: The two women are neighbors.
#  3: The two women are business partners.
# Program:
# SUBTITLES=GetSubtitles(video=VIDEO_ID)
# VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=None, query=None)
# VIDEO_SEARCH_RESULT_1=SearchVideo(video=VIDEO_ID, timestamp=None, query="Describe the mood of the people in the image")
# TEXT_SEARCH_RESULT_1=EvaluateText(text=SUBTITLES, query="Does the conversation seem to be business or personal?")
# SEARCH_RESULT_TEXT=ConcatenateText(text1=VIDEO_SEARCH_RESULT_1, text2=TEXT_SEARCH_RESULT_1)
# FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, additional_context=SEARCH_RESULT_TEXT)
# RESULT=EvaluateText(text=FINAL_TEXT, query="What is the most likely choice from the given options? Respond in the format 'answer_idx: index of the option, answer_text: text of the option'")
# """,
# """
# Question: Does the interviewee seem to be confident in his answers?
# Options:
#  0: The interviewee is nervous about his responses.
#  1: No, he seems very unsure
#  2: The interviewee is charismatic and confident in his responses to the interviewer.
#  3: The man in the blue shirt is wearing mismatched socks.
# Program:
# SUBTITLES=GetSubtitles(video=VIDEO_ID)
# VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=None, query=None)
# VIDEO_SEARCH_RESULT_1=SearchVideo(video=VIDEO_ID, timestamp=None, query="Does the interviewee look confident?")
# TEXT_SEARCH_RESULT_1=EvaluateText(text=SUBTITLES, query="Do the people in the conversation seem confident?")
# SEARCH_RESULT_TEXT=ConcatenateText(text1=VIDEO_SEARCH_RESULT_1, text2=TEXT_SEARCH_RESULT_1)
# FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, additional_context=SEARCH_RESULT_TEXT)
# RESULT=EvaluateText(text=FINAL_TEXT, query="What is the most likely choice from the given options? Respond in the format 'answer_idx: index of the option, answer_text: text of the option'")
# """,
# """
# Question: What is the demeanor of the lady like?
# Options:
#  0: The woman is calm and composed.
#  1: she is open to talk
#  2: The woman sounds engaged and friendly.
#  3: She is very serious.
# Program:
# SUBTITLES=GetSubtitles(video=VIDEO_ID)
# VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=None, query=None)
# VIDEO_SEARCH_RESULT_1=SearchVideo(video=VIDEO_ID, timestamp=None, query="What is the mood of the woman?")
# TEXT_SEARCH_RESULT_1=EvaluateText(text=SUBTITLES, query="Summarize the overall tone of the conversation with respect to the lady")
# SEARCH_RESULT_TEXT=ConcatenateText(text1=VIDEO_SEARCH_RESULT_1, text2=TEXT_SEARCH_RESULT_1)
# FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, additional_context=SEARCH_RESULT_TEXT)
# RESULT=EvaluateText(text=FINAL_TEXT, query="What is the most likely choice from the given options? Respond in the format 'answer_idx: index of the option, answer_text: text of the option'")
# """,
"""
Question: How does the man show how he feels about what he is saying?
Options:
 0: He frowns as he speaks and lowers his tone while using open body language.
 1: The man taps his foot impatiently while he speaks because he has somewhere else to be.
 2: The man furrows his brow while he speaks because he is trying to remember the details.
 3: He smiles as he speaks and raises his tone while using open body language.
Program:
SUBTITLES=GetSubtitles(video=VIDEO_ID)
VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=None, query=None)
VIDEO_SEARCH_RESULT_1=SearchVideo(video=VIDEO_ID, timestamp=None, query="What is the body language of the man?")
VIDEO_SEARCH_RESULT_2=SearchVideo(video=VIDEO_ID, timestamp=None, query="Does the man tap his foot impatiently?")
VIDEO_SEARCH_RESULT_3=SearchVideo(video=VIDEO_ID, timestamp=None, query="Does the man appear calm?")
TEXT_SEARCH_RESULT_1=EvaluateText(text=SUBTITLES, query="Summarize the overall conversation")
SEARCH_RESULT_TEXT=ConcatenateText(text1=VIDEO_SEARCH_RESULT_1, text2=VIDEO_SEARCH_RESULT_2, text3=VIDEO_SEARCH_RESULT_3, text4=TEXT_SEARCH_RESULT_1)
FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, additional_context=SEARCH_RESULT_TEXT)
RESULT=EvaluateText(text=FINAL_TEXT, query="What is the most likely choice from the given options? Respond in the format 'answer_idx: index of the option, answer_text: text of the option'")
""",
"""
Question: Are the two people happy to be together?
Options:
 0: The two people are arguing with each other.
 1: The video shows people dancing in a club.
 2: They want to stay.
 3: Yes, they are enjoying this time together.
Program:
SUBTITLES=GetSubtitles(video=VIDEO_ID)
VIDEO_DESCRIPTION=DescribeVideo(video=VIDEO_ID, timestamp=None, query=None)
VIDEO_SEARCH_RESULT_1=SearchVideo(video=VIDEO_ID, timestamp=None, query="Do the two people appear happy?")
TEXT_SEARCH_RESULT_1=EvaluateText(text=SUBTITLES, query="Do the two people appear to be happy?")
SEARCH_RESULT_TEXT=ConcatenateText(text1=VIDEO_SEARCH_RESULT_1, text2=TEXT_SEARCH_RESULT_1)
FINAL_TEXT=CreateText(question=QUESTION, subtitles=SUBTITLES, video_description=VIDEO_DESCRIPTION, additional_context=SEARCH_RESULT_TEXT)
RESULT=EvaluateText(text=FINAL_TEXT, query="What is the most likely choice from the given options? Respond in the format 'answer_idx: index of the option, answer_text: text of the option'")
"""
]

def create_prompt(inputs,num_prompts=8,method='random',seed=42,group=0):
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