import os

import cv2


global i

class VideoWriter:
    def __init__(self, vid_fps, vid_width, vid_height, filename="out", vid_format="mov"):
        global i
        self.fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')

        self.vid_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'newsBcasterBroadcaster/static/')

        self.out = cv2.VideoWriter(self.vid_dir + filename + '.' + vid_format, self.fourcc, float(vid_fps),
                                   (int(float(vid_width)), int(float(vid_height))))

        self.out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'newsBcasterBroadcaster/static/out/')

        for file in os.listdir(self.out_dir):
            file_remove = os.path.join(self.out_dir, file)
            try:
                if os.path.isfile(file_remove):
                    os.unlink(file_remove)
            except Exception, e:
                print e


        i = 0

    def writer(self, frame):
        global i
        cv2.imwrite(self.out_dir + str(i) + ".jpg", frame)
        i += 1
        self.out.write(frame)
