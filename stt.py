# Google's speech to text API

import requests
from creds import GOOGLE_API
import subprocess
import sys

# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
# 'google-cloud-speech'])

from google.cloud import speech

# from google.cloud import speech_v1
# from google.cloud.speech_v1 import types

def speech_to_text(filename = "temp/test_recording.mp3"):
    client = speech.SpeechClient.from_service_account_file('google.json')


    with open(filename, 'rb') as f:
        mp3_data = f.read()

    audio_file = speech.RecognitionAudio(content=mp3_data)
    config = speech.RecognitionConfig(
        sample_rate_hertz = 48000,
        enable_automatic_punctuation=True,
        language_code='en-US'
    )

    response = client.recognize(
        config=config,
        audio=audio_file
    )
    # print(response)
    # ALTHOUGH STT RETURNS MULTIPLE PHRASES, I JUST WANT THE FIRST ONE

    best_alternative = response.results[-1].alternatives[0]
    transcript = best_alternative.transcript
    confidence = best_alternative.confidence
    print("-" * 80)
    print(f"Transcript: {transcript}")
    print(f"Confidence: {confidence:.0%}")
    return best_alternative

# speech_to_text(filename="temp/post_output.mp3")


# import os
# import ffmpeg

# def convert_wav_to_mp3(wav_file_path, mp3_file_path):
#     abs_wav_file_path = os.path.abspath(wav_file_path)
#     abs_mp3_file_path = os.path.abspath(mp3_file_path)
#     print(abs_mp3_file_path, abs_wav_file_path)
#     stream = ffmpeg.input(abs_wav_file_path)
#     stream = ffmpeg.output(stream, abs_mp3_file_path, codec='libmp3lame', qscale=2)
#     ffmpeg.run(stream)

# convert_wav_to_mp3('output.wav', 'output.mp3')