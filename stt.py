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

def speech_to_text(filename = "test_recording.wav"):
    client = speech.SpeechClient.from_service_account_file('google.json')


    with open(filename, 'rb') as f:
        mp3_data = f.read()

    audio_file = speech.RecognitionAudio(content=mp3_data)
    config = speech.RecognitionConfig(
        sample_rate_hertz = 44100,
        enable_automatic_punctuation=True,
        language_code='en-US'
    )

    response = client.recognize(
        config=config,
        audio=audio_file
    )
    # print(response)
    # ALTHOUGH STT RETURNS MULTIPLE PHRASES, I JUST WANT THE FIRST ONE
    for result in response.results:
        best_alternative = result.alternatives[0]
        transcript = best_alternative.transcript
        confidence = best_alternative.confidence
        print("-" * 80)
        print(f"Transcript: {transcript}")
        print(f"Confidence: {confidence:.0%}")
    return transcript

speech_to_text()


# with open(filename, "rb") as f:
#     audio = f.read()

# config = dict(language_code="en-US")


# audio = {"content": audio}

# response = client.recognize(config=config, audio=audio)

# for result in response.results:
#     best_alternative = result.alternatives[0]
#     transcript = best_alternative.transcript
#     confidence = best_alternative.confidence
#     print("-" * 80)
#     print(f"Transcript: {transcript}")
#     print(f"Confidence: {confidence:.0%}")