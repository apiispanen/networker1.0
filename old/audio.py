import pyaudio
import wave

# set up PyAudio
p = pyaudio.PyAudio()

# open a stream to record audio
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)

# start recording
frames = []
for i in range(0, int(16000)):
    data = stream.read(1024)
    frames.append(data)

# stop recording
stream.stop_stream()
stream.close()
p.terminate()

# save the recorded audio to a file
wf = wave.open("output.wav", "wb")
wf.setnchannels(1)
wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
wf.setframerate(16000)
wf.writeframes(b"".join(frames))
wf.close()
