import socket
import pickle

import cv2


TCP_IP = "localhost"
TCP_PORT = 5000
BUFFER_SIZE = 4096
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.bind((TCP_IP, TCP_PORT))
connection.listen(1)
conn, addr = connection.accept()
i = 0
while True:
    vid_metadata = str(connection.recv(1024))

    # noinspection PyRedeclaration
    num_frames, sep, vid_metadata = vid_metadata.partition(';;')

    # noinspection PyRedeclaration
    vid_width, sep, vid_metadata = vid_metadata.partition('::')

    # noinspection PyRedeclaration
    vid_height, sep, vid_fps = vid_metadata.partition('??')

    num_frames = int(float(num_frames))
    if vid_metadata:
        connection.sendall(b'OK')
        break

fourcc = cv2.cv.CV_FOURCC(*'XVID')
# noinspection PyUnboundLocalVariable
out = cv2.VideoWriter('out.avi', fourcc, float(vid_fps), (int(float(vid_width)), int(float(vid_height))))
while True:
    length = None
    message = ""
    while True:
        data = connection.recv(BUFFER_SIZE)
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
                print "Received Status : OK"
                break
            elif len(message) > length:
                print "Recieved Status : Over"
                break
            else:
                continue

    connection.sendall(b'FINFRAME')
    i += 1
    print "Now in frame : " + str(i)
    frame = pickle.loads(message)
    out.write(frame)
    if i == num_frames or i > num_frames:
        break

connection.close()
