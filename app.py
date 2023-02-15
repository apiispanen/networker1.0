import pyaudio
import wave
import os
from stt import speech_to_text
from prompt import *
from tts import tts
# import subprocess
# import sys
# import pydub
from flask import Flask, request, render_template, jsonify
from sound import *


print('enter getJSONReuslt', flush=True)

app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"

@app.route('/')
def index():
    return render_template('indexs.html')

@app.route('/startRecording')
def startRecording(guiAUD=guiAUD):
    guiAUD.startRecording()
    return "On"

@app.route('/stopRecording')
def stopRecording(guiAUD=guiAUD):
    guiAUD.stopRecording()
    text_result = speech_to_text()
    transcript = text_result.transcript
    confidence = text_result.confidence 
    response = ai_response(transcript)
    tts(response)
    return 'Off'
    

@app.route("/save_audio", methods=['POST'])
def save_audio():
    # Original function
    audio = request.data
    filename = 'temp/post_output.mp3'
    with open(filename, "wb") as f:
        f.write(audio)
    f.close()
    ### Check if file is present: 
    # if os.path.isfile(filename) and os.access(filename, os.W_OK):
    #     print(f"{filename} exists and is writable")
    # else:
    #     print(f"{filename} either does not exist or is not writable")

    
    # original function END
    # pydub.AudioSegment.export(filename, format="mp3")

    # stt_object = speech_to_text(filename=filename)
    # transcript, confidence = stt_object.transcript, stt_object.confidence
    # print(transcript, confidence)
    # print("Thinking...")
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
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)


# ai_response("What are 5 words to describe a grouchy fucking pig?")