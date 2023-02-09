import pyaudio
import wave
import os
# from stt import speech_to_text
# from prompt import *
# from tts import tts
# import subprocess
# import sys

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/save_audio", methods=['POST'])
def save_audio():
    audio = request.data
    with open("output.wav", "wb") as f:
        f.write(audio)
    return "Audio saved."

if __name__ == "__main__":
    app.run(debug=True)


# ai_response("What are 5 words to describe a grouchy fucking pig?")