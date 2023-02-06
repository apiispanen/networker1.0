import requests
from creds import API_KEY
import subprocess
import sys
# import ssl
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
# 'openai'])

# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
# 'ssl'])

import openai
import json

def ai_response(prompt, networking = False, previous_conversation=None, API_KEY = API_KEY):
    openai.api_key = API_KEY

    model_engine = "text-davinci-002"

    if networking:
        prompt = "Can you make me an Object oriented response in JSON for a database table called 'people' that contains as much specific information about interests, facts, and any cool thoughts about the person who is described in the dialog below: " + prompt

    if previous_conversation:
        # prompt = f"This is the Python Dictionary of all our previous conversations, logged as 'Question by me : Answer by you. Please read this before I ask the question, at the bottom.': {previous_conversation} Based on the JSON from before, {prompt}"
        prompt = f"This is a Python Dictionary of all my previous prompts to you in chronological order, logged as a Python Dictionary (format is 'Prompt #':'Prompt'). These are only questions or words I have already inquiried with you (prompts). Please take all this into consideration after I ask the question below.\n {previous_conversation}. \n\nPrompt: {prompt}"


    # print(prompt)


    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=2,
        stop=None,
        temperature=0.5,
        frequency_penalty=1
    )

    message = completions.choices[0].text
    return message



def save_conversation(prompt, response=None):
    
    filename = 'temp/conversation.json'

    with open(filename) as fp:
        listObj = json.load(fp)
        
    # Verify existing list
    # print(listObj)

    # request_num = str(len(listObj) /2)
    listObj["prompt "+str(len(listObj))] = prompt
    # listObj["response "+request_num] = response
    
    # Verify updated list
    # print(listObj)

    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file, 
                            indent=4,  
                            separators=(',',': '), ensure_ascii=True)





def load_conversation():
    try:
        with open("temp/conversation.json", "r") as f:
            all_prompts = json.load(f)
            # print(all_prompts)
            return all_prompts
    except:
        return {}


# prompt="What is my name?"

# """I'm writing a script that will log relevant information about a person. Can you highlight the conversation below with the following format?
# - Person 
# - Occupation (if applicable)
# - Company (if applicable)
# - Interesting facts (if applicable)

# Conversation below:
# "I just met Sam Casey who is an engineer designing his own app with ChatGPT. He currently works with a company called Mercury who does NFT development, which is very interesting. he gave me his email, but I can't read it. I also found that we share the name college - both of us went to Babson. He'll be back in San Francisco in a few months, so maybe I can meet with him then."
# """

# conversation = ai_response(prompt, previous_conversation=load_conversation())

# print(conversation)

# save_conversation(prompt, conversation)