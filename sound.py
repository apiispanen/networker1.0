# Import the necessary modules.
import subprocess
import sys
from stt import speech_to_text
from prompt import ai_response, save_conversation
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
# 'ttkthemes'])


import pyaudio
import wave
import os


class RecAUD:
    recording_done = False
    def __init__(self, chunk=3024, frmat=pyaudio.paInt16, channels=1, rate=48000, py=pyaudio.PyAudio()):
        self.collections = []
        self.CHUNK = chunk
        self.FORMAT = frmat
        self.CHANNELS = channels
        self.RATE = rate
        self.p = py
        self.frames = []
        self.st = 1
        self.stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)


    def add_response(self, transcript, response, confidence):
        text = "\n\nTranscript: {}\nConfidence: {} \n\nResponse: {}".format(transcript, confidence, response)
        self.response = response

    def startRecording(self):
        print("* recording")
        self.st = 1
        self.frames = []
        while self.st == 1:
            data = self.stream.read(self.CHUNK)
            self.frames.append(data)

    def stopRecording(self):
        print("* done recording")
        self.st = 0
        self.stream.stop_stream()
        self.stream.close()
        wf = wave.open("temp/test_recording.mp3", "wb")
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b"".join(self.frames))
        wf.close()

# p = pyaudio.PyAudio()

# for i in range(p.get_device_count()):
#     dev = p.get_device_info_by_index(i)
#     print((i,dev['name'],dev['maxInputChannels']))



# Create an object of the ProgramGUI class to begin the program.
guiAUD = RecAUD()
