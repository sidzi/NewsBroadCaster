import wave

CHUNK = 1024
CHANNELS = 2
RATE = 44100
WAVE_OUT_NAME = "out.wav"


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