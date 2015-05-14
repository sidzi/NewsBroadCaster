import wave
import os

CHUNK = 1024
CHANNELS = 2
RATE = 44100
WAVE_OUT_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'newsBcasterBroadcaster/static/') + str(
    "out.wav")


def write(frames):
    """
    :rtype : None
    """
    wf = wave.open(WAVE_OUT_NAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(2)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()