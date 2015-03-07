import socket
import cv2
import ast

TCP_IP = '127.0.0.1'
TCP_PORT = 5006
BUFFER_SIZE = 1024
MESSAGE = "Acknowledgement"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
while 1:
    data = s.recv(BUFFER_SIZE)
    # data = [n.strip() for n in data]
    # print "received data:", data
    # cv2.namedWindow("preview")
    # cv2.imshow("preview", data)
    print data
    s.send(MESSAGE)
    if not data:
        break
s.close()

