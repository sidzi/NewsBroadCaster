import socket
import pickle

import cv2


TCP_IP = "localhost"
TCP_PORT = 5000
BUFFER_SIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
frame = cv2.imread("hello.png")
conn, addr = s.accept()
print 'Connection address:', addr
while True:
    data = pickle.dumps(frame)
    datawithlength = str(len(data)) + ':::::' + data
    print datawithlength
    conn.send(datawithlength)
    if str(conn.recv(BUFFER_SIZE)) == "FINISH":
        break

conn.close()
