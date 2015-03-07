import socket
import cv2
import numpy

cap = cv2.VideoCapture('lmao.mp4')
TCP_IP = '127.0.0.1'
TCP_PORT = 5006
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    ret, frame = cap.read()
    size = len(frame)
    size = str(size)
    conn.send(size)
    # str1 = ''.join(str(e) for e in frame)
    # conn.send(str1)
    # data = [n.strip() for n in data]
    # print data
    # ender = 0
    # ender = str(ender)
    # conn.send(ender)
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
cap.release()
cv2.destroyAllWindows()
conn.close()