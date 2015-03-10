import socket
import pickle

import cv2


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 5000
BUFFER_SIZE = 4096

s.connect((host, port))
i = 1
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
        print "Size of the frame : " + length_str + "\n"
        length = int(length_str)

    if len(message) < length:
        message += data
        print "Appending ... " + str(i)
        i += 1
        if len(message) == length:
            print "Received Status OK"
            break
        elif len(message) > length:
            print "Recieved Status Overload"
            break
        else:
            s.sendall("1")
            continue

s.sendall("FINISH")
s.close()
frame = pickle.loads(message)
print frame
cv2.imshow('Recieved image', frame)
cv2.waitKey(2500)
cv2.destroyAllWindows()

