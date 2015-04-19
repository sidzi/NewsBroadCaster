import socket
import pickle
import wave
import os

from VideoReader import videoReader


class BcastClient:
    def __init__(self, filepath, overlay_text):
        self.TCP_IP = 'localhost'
        self.TCP_PORT = 5000
        self.BUFFER_SIZE = 4096
        self.SMALL_BUFFER = 128
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((self.TCP_IP, self.TCP_PORT))
        self.video = videoReader(filepath)
        self.cap = self.video.getcap()
        self.wf = wave.open(filepath + "_audio.wav", 'rb')
        self.audio_size = os.path.getsize(filepath + "_audio.wav")
        self.o_text = overlay_text

    def send_video(self):
        # Overlay Transfer Here
        self.connection.send(b'1')
        if 'ok' in self.connection.recv(4):
            while True:
                self.connection.send(self.o_text)
                if "OK" in str(self.connection.recv(self.SMALL_BUFFER)):
                    break
            # Video Transferring Here
            while True:
                self.connection.send(
                    "{0};;{1}::{2}??{3}".format(self.video.frame_count, self.video.frame_width, self.video.frame_height,
                                                self.video.frames_per_sec))
                if "OK" in str(self.connection.recv(self.SMALL_BUFFER)):
                    break
            while self.cap.isOpened():
                ret, frame = self.cap.read()
                if not ret:
                    break
                while ret:
                    data = pickle.dumps(frame)
                    datawithlength = str(len(data)) + '::' + data
                    self.connection.send(datawithlength)
                    end_of_frame = str(self.connection.recv(self.BUFFER_SIZE))
                    if "FINFRAME" in end_of_frame:
                        break
            self.connection.send("EOVT")
            self.send_audio()

    def send_audio(self):
        # Audio Transferring Here
        self.connection.send(b'2')
        if 'RRA' in self.connection.recv(self.SMALL_BUFFER):
            self.connection.send(str(self.audio_size))
            audio_data = self.wf.readframes(self.BUFFER_SIZE)
            while audio_data != '':
                while True:
                    audio_data_dup = pickle.dumps(audio_data)
                    audio_data_wlen = str(len(audio_data_dup)) + '::' + audio_data_dup
                    self.connection.send(audio_data_wlen)
                    end_of_aframe = str(self.connection.recv(self.BUFFER_SIZE))
                    if 'FINFRAME' in end_of_aframe:
                        break
                audio_data = self.wf.readframes(self.BUFFER_SIZE)
            self.connection.send(b'ENDALL')
            self.connection.send(b'End')

    def start_broadcast(self):
        self.connection.send(b'3')

    def stop_broadcast(self):
        self.connection.send(b'0')

    def close(self):
        self.video.close()
        self.connection.close()