import wave
import sys

import pyaudio


class AudioRecorder:
    def __init__(self, time):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.RECORD_SEC = time
        self.WAVE_OUT_NAME = "out_rec.wav"

    def record(self):
        if sys.platform == 'darwin':
            self.CHANNELS = 1

        p = pyaudio.PyAudio()

        stream = p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True,
                        frames_per_buffer=self.CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SEC)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(self.WAVE_OUT_NAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()