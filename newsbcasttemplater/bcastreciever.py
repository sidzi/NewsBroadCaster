import socket
import pickle

import cv2


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('out.avi', fourcc, 25.0, (320, 180))

host = "localhost"
port = 5000
BUFFER_SIZE = 4096

s.connect((host, port))
i = 1

while True:
    length = None
    message = ""
    while True:
        data = s.recv(BUFFER_SIZE)
        if not data:
            break
        if length is None:
            if '::' not in data:
                break

            length_str, ignored, data = data.partition('::')
            print "\nSize of the frame : " + length_str
            length = int(length_str)

        if len(message) < length:
            message += data
            if len(message) == length:
                print "Received Status OK"
                break
            elif len(message) > length:
                print "Recieved Status Overload"
                break
            else:
                continue

    s.sendall(b'FINFRAME')
    print "Now in frame : " + str(i)
    frame = pickle.loads(message)
    out.write(frame)
    i += 1

cv2.destroyAllWindows()
s.close()

