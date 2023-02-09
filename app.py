import pyaudio
import wave
import os
from stt import speech_to_text
from prompt import *
from tts import tts
# import subprocess
# import sys

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/save_audio", methods=['POST'])
def save_audio():
    # Original function
    audio = request.data
    filename = 'temp/post_output.wav'
    with open(filename, "wb") as f:
        f.write(audio)
    f.close()
    
    # original function END

    stt_object = speech_to_text(filename=filename)
    transcript, confidence = stt_object.transcript, stt_object.confidence
    print(transcript, confidence)
    print("Thinking...")
    return "Audio saved."

    # return transcript


    # response = ai_response(transcript)
    # # response = ai_response(transcript, previous_conversation=load_conversation())

    # save_conversation(transcript)

    # print(response)

    # # ADD THE TEXT CONFIDENCE AND RESPONSE TO THE PROMPT
    # # self.add_response(transcript, response, confidence)
    # tts(response)








if __name__ == "__main__":
    app.run(debug=True)


# ai_response("What are 5 words to describe a grouchy fucking pig?")