import socket
import pickle

import cv2


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 5000
BUFFER_SIZE = 4096

s.connect((host, port))
i = 0
length = None
message = ""
while True:
    data = s.recv(1024)
    if not data:
        break
    while True:
        if length is None:
            if ':::::' not in data:
                break

            length_str, ignored, data = data.partition(':::::')
            print length_str + " LOL " + ignored + "LOP\n"
            length = int(length_str)

        if len(message) < length:
            message += data
            print "Appending..." + str(i)
            i += 1
            s.sendall("1")
        else:
            print "complete recv" + str(len(message) == length)
            break
    s.sendall("FINISH")

    frame = pickle.loads(message)
    print frame
    cv2.imshow('Recieved image', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
s.close()
