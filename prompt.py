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

def ai_response(prompt, API_KEY = API_KEY):
    openai.api_key = API_KEY

    model_engine = "text-davinci-002"
    
    """I'm writing a script that will log relevant information about a person. Can you highlight the conversation below with the following format?
    - Person 
    - Occupation (if applicable)
    - Company (if applicable)
    - Interesting facts (if applicable)

    Conversation below:
    "I just met Sam Casey who is an engineer designing his own app with ChatGPT. He currently works with a company called Mercury who does NFT development, which is very interesting. he gave me his email, but I can't read it. I also found that we share the name college - both of us went to Babson. He'll be back in San Francisco in a few months, so maybe I can meet with him then."
    """

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message
    # 