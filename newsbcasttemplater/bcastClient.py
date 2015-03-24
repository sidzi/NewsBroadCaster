import socket
import pickle

from videoReader import videoReader


class BcastClient:
    def __init__(self, filepath):
        self.TCP_IP = 'localhost'
        self.TCP_PORT = 5000
        self.BUFFER_SIZE = 4096
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((self.TCP_IP, self.TCP_PORT))
        self.video = videoReader(filepath)
        self.cap = self.video.getcap()

    def run(self):
        while True:
            self.connection.send(
                "{0};;{1}::{2}??{3}".format(self.video.frame_count, self.video.frame_width, self.video.frame_height,
                                            self.video.frames_per_sec))
            if "OK" in str(self.connection.recv(128)):
                break
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break
            while ret:
                data = pickle.dumps(frame)
                datawithlength = str(len(data)) + '::' + data
                print str(len(data))
                self.connection.send(datawithlength)
                end_of_frame = str(self.connection.recv(self.BUFFER_SIZE))
                if "FINFRAME" in end_of_frame:
                    break
        self.close()

    def close(self):
        self.video.close()
        self.connection.close()