import subprocess


def extract(filepath="lmao.mp4"):
    command = "ffmpeg -i " + str(filepath) + " -ab 160k -ac 2 -ar 44100 -vn " + filepath + "_audio.wav"
    subprocess.call(command, shell=True)
