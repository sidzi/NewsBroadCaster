import socket
import pickle

import cv2


TCP_IP = "localhost"
TCP_PORT = 5000
BUFFER_SIZE = 4096


class BcastClient:
    def __init__(self):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((TCP_IP, TCP_PORT))
        # noinspection PyArgumentList
        cap = cv2.VideoCapture("lmao.mp4")
        while True:
            connection.send(str(cap.get(7)) + ";;" + str(cap.get(3)) + "::" + str(cap.get(4)) + "??" + str(cap.get(5)))
            if "OK" in str(connection.recv(128)):
                break

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            while ret:
                data = pickle.dumps(frame)
                datawithlength = str(len(data)) + '::' + data
                print str(len(data))
                connection.send(datawithlength)
                end_of_frame = str(connection.recv(BUFFER_SIZE))
                if "FINFRAME" in end_of_frame:
                    print end_of_frame
                    break
        cap.release()
        connection.close()
