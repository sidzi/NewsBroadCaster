import wave
import sys

from pyaudio import PyAudio


CHUNK = 1024

if len(sys.argv) < 2:
    print("plays a wave file.\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

p = PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()

p.terminate()
