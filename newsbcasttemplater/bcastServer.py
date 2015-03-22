import socket
import pickle

import cv2


class BcastServer:
    def __init__(self):
        self.TCP_IP = 'localhost'
        self.TCP_PORT = 5000
        self.BUFFER_SIZE = 4096
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.bind((self.TCP_IP, self.TCP_PORT))
        self.connection.listen(5)
        self.connected_host, addr = self.connection.accept()

    def close(self):
        self.connected_host.close()

    def run(self):
        i = 0
        while True:
            vid_metadata = str(self.connected_host.recv(1024))

            # noinspection PyRedeclaration
            num_frames, sep, vid_metadata = vid_metadata.partition(';;')

            # noinspection PyRedeclaration
            vid_width, sep, vid_metadata = vid_metadata.partition('::')

            # noinspection PyRedeclaration
            vid_height, sep, vid_fps = vid_metadata.partition('??')

            num_frames = int(float(num_frames))
            if vid_metadata:
                self.connected_host.send(b'OK')
                break

        fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
        # noinspection PyUnboundLocalVariable
        out = cv2.VideoWriter('out.mov', fourcc, float(vid_fps), (int(float(vid_width)), int(float(vid_height))))
        while True:
            length = None
            message = ""
            while True:
                data = self.connected_host.recv(self.BUFFER_SIZE)
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

            self.connected_host.send(b'FINFRAME')
            i += 1
            print "Now in frame : " + str(i)
            frame = pickle.loads(message)
            out.write(frame)
            if i == num_frames or i > num_frames:
                break


if __name__ == "__main__":
    bCS = BcastServer()
    bCS.run()
    bCS.close()