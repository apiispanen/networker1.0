# Import the necessary modules.
import tkinter
import tkinter as tk
import tkinter.messagebox
import subprocess
import sys
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
# 'ttkthemes'])

from ttkthemes import ThemedTk

import pyaudio
import wave
import os
from stt import speech_to_text
from prompt import ai_response


class RecAUD:
    recording_done = False
    def __init__(self, chunk=3024, frmat=pyaudio.paInt16, channels=1, rate=44100, py=pyaudio.PyAudio()):
        
        def button_hold_callback(event,self=self):
            print("holding")
            # PLEASE ADD RECORDING START HERE
            self.start_record()

        def button_release_callback(event,self=self):
            print("Button released")
            self.stop()
            # PLEASE ADD RECORDING STOP HERE

        # Start Tkinter and set Title
        # self.main = tkinter.Tk()
        self.main = ThemedTk(theme="arc")
        self.collections = []
        self.main.geometry('500x600')
        self.main.title('Record')
        self.CHUNK = chunk
        self.FORMAT = frmat
        self.CHANNELS = channels
        self.RATE = rate
        self.p = py
        self.frames = []
        self.st = 1
        self.stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        self.T = tk.Text(self.main, height=20, width=30, wrap="word")
        self.T.pack()
        self.T.insert(tk.END, "Your Answers will show up here")
        # Set Frames
        self.buttons = tkinter.Frame(self.main, padx=120, pady=20)
        # Pack Frame
        self.buttons.pack(fill=tk.BOTH)

        # Start and Stop buttons
        self.strt_rec = tkinter.Button(self.buttons, width=10, padx=10, pady=5, text='Record')
        # ADD THE FUNCTION IN ABOVE: command=lambda: self.start_record()
        self.strt_rec.grid(row=0, column=0, padx=50, pady=5)
        self.strt_rec.bind('<ButtonPress-1>', button_hold_callback)
        self.strt_rec.bind("<ButtonRelease-1>", button_release_callback)
        tkinter.mainloop()
        
    def add_text(self, transcript, response, confidence):
            # ADDS TEXT TO THE PROMPT
            # T = tk.Text(self.main, height=10, width=30)
            # T.pack()
            text = "\n***********\nTranscript: {}\nConfidence: {} \n\nResponse: {}".format(transcript, confidence, response)
            self.T.insert(tk.END, text)
            self.T.see(tk.END)

    def start_record(self):
        self.st = 1
        self.frames = []
        stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        print("* recording")
        self.strt_rec.config(relief=tk.SUNKEN)

        while self.st == 1:
            data = stream.read(self.CHUNK)
            self.frames.append(data)
            self.main.update()

        stream.close()

        # SAVE THE RECORDING
        wf = wave.open('test_recording.wav', 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        self.recording_done = True
        # print(ai_response("How many people are there in Germany?"))


        # NOW RUN IT THROUGH STT
        stt_object = speech_to_text()
        transcript, confidence = stt_object.transcript, stt_object.confidence

        # AND MOVE IT TO OPEN AI
        print("Thinking...")
        response = ai_response(transcript)
        print(response)

        # ADD THE TEXT CONFIDENCE AND RESPONSE TO THE PROMPT
        self.add_text(transcript, response, confidence)


    def stop(self):
        print("*** STOPPED ****")
        self.strt_rec.config(relief=tk.RAISED)
        self.st = 0
        

# Create an object of the ProgramGUI class to begin the program.
guiAUD = RecAUD()