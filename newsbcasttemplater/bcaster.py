import socket
import pickle

import cv2


TCP_IP = "localhost"
TCP_PORT = 5000
BUFFER_SIZE = 4096
# noinspection PyArgumentList
cap = cv2.VideoCapture("lmao.mp4")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connection address:', addr

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    data = datawithlength = ""
    while True:
        data = pickle.dumps(frame)
        datawithlength = str(len(data)) + '::' + data
        print str(len(data))
        conn.send(datawithlength)
        end_of_frame = str(conn.recv(BUFFER_SIZE))
        if "FINFRAME" in end_of_frame:
            print end_of_frame
            break
cap.release()
conn.close()
