import numpy as np
import cv2
import socket

cap = cv2.VideoCapture('lmao.mp4')
i = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 6556
s.bind((host, port))
while True:
    msg, addr = s.recv(8192)
    print "got conn from",addr
    while i < 25:
        # Capture frame-by-frame
        ret, frame = cap.read()

        print frame
        i += 1
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imwrite('sill.jpeg', frame)
        # Display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
