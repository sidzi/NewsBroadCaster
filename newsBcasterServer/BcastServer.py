import socket
import pickle
import threading

from VideoWriter import VideoWriter
import overlayer
import AudioWriter
from newsBcasterServer.newsBcasterBroadcsater.app import app


class BcastServer:
    def __init__(self):
        """
        :rtype : BcastServer
        """
        self.TCP_IP = 'localhost'
        self.TCP_PORT = 5000
        self.BUFFER_SIZE = 4096
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.bind((self.TCP_IP, self.TCP_PORT))
        self.connection.listen(10)
        self.rec_file_size = 0
        self.SMALL_BUFFER = 100
        self.threads = []

    def accept_connections(self):
        while True:
            connected_host, addr = self.connection.accept()
            t = threading.Thread(self.run(connected_host))
            t.start()
            self.threads.append(t)
        for t in self.threads:
            t.join()

    def recieve_video(self, conn_host):
        # overlay text
        overlay_text = str(conn_host.recv(self.BUFFER_SIZE))
        if overlay_text:
            conn_host.send(b'OK')
        # global vid_metadata
        i = 0
        vid_metadata = str(conn_host.recv(self.BUFFER_SIZE))
        if vid_metadata:
            conn_host.send(b'OK')
        # noinspection PyRedeclaration
        num_frames, sep, vid_metadata = vid_metadata.partition(';;')

        # noinspection PyRedeclaration
        vid_width, sep, vid_metadata = vid_metadata.partition('::')

        # noinspection PyRedeclaration
        vid_height, sep, vid_fps = vid_metadata.partition('??')

        num_frames = int(float(num_frames))

        vw = VideoWriter(vid_fps, vid_width, vid_height)

        overlayer.getwandh(int(float(vid_width)), int(float(vid_height)))

        while True:
            length = None
            message = ""
            while True:
                data = conn_host.recv(self.BUFFER_SIZE)
                if not data:
                    break
                if length is None:
                    if '::' not in data:
                        break

                    length_str, ignored, data = data.partition('::')
                    print '\nSize of the frame : {0}'.format(str(int(length_str) / 1024 * 8))
                    length = int(length_str)

                if len(message) < length:
                    message += data
                    if len(message) == length:
                        print 'Received Status : OK'
                        break
                    elif len(message) > length:
                        print 'Recieved Status : Over'
                        break
                    else:
                        continue

            conn_host.send(b'FINFRAME')
            i += 1
            print 'Writing frame : {0}'.format(str(i))
            frame = pickle.loads(message)
            frame = overlayer.overlay(frame, i, overlay_text)
            vw.writer(frame)
            if i == num_frames or i > num_frames:
                break

    def recieve_audio(self, conn_host):
        # Ready to recieve audio
        conn_host.send(b'RRA')
        file_size = int(conn_host.recv(self.SMALL_BUFFER))
        i = 1
        flag = 0
        audio_frames = []
        while True:
            print('FILE SIZE = {0}'.format(str(file_size / (1024))))
            length_audio = None
            audio_frame = ""
            while True:
                audio_data = conn_host.recv(self.BUFFER_SIZE)
                if not audio_data or 'ENDALL' in audio_data:
                    flag = 1
                    break
                if length_audio is None:
                    if '::' not in audio_data:
                        print "Siper Error I dont Which"
                        break

                    length_audio, sep, audio_data = audio_data.partition('::')
                    length_audio = int(length_audio)
                    print '\nSize : {0}'.format(str(length_audio / (1024)))

                if len(audio_frame) < length_audio:
                    audio_frame += audio_data
                    if len(audio_frame) == length_audio:
                        print("Chunk Received Status : OK\nChunk # = " + str(i))
                        i += 1
                        break
                    elif len(audio_frame) > length_audio:
                        print("Overload")
                        break
            if flag:
                break

            audio_frame = pickle.loads(audio_frame)
            self.rec_file_size += len(audio_frame)
            audio_frames.append(audio_frame)
            conn_host.send(b'FINFRAME')

        AudioWriter.write(audio_frames)

    def run(self, conn_host):

        while True:
            choice = conn_host.recv(32)
            choice = int(choice)
            if choice is 0:
                break
            elif choice is 1:
                conn_host.send(b'ok')
                self.recieve_video(conn_host)
                if not 'EOVT' in str(conn_host.recv(self.SMALL_BUFFER)):
                    print "Error in recieving complete video"
                    break

            elif choice is 2:
                conn_host.send(b'ok')
                self.recieve_audio(conn_host)
                if not 'End' in conn_host.recv(self.SMALL_BUFFER):
                    print "Error in recieving complete audio"
                    break
            elif choice is 3:
                app.run(self.TCP_IP, 8000)
        conn_host.close()


if __name__ == "__main__":
    bCS = BcastServer()
    print("Server Started at\nIP : " + str(bCS.TCP_IP) + "\nPort : " + str(bCS.TCP_PORT))
    bCS.accept_connections()