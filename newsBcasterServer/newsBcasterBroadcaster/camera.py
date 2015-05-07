from time import sleep
import os

global i


class Camera(object):
    def __init__(self):
        global i
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
        self.frame_count = int(len(os.listdir(out_dir + "/out")))
        self.frames = [open(out_dir + "/out/" + str(f) + '.jpg', 'rb').read() for f in list(xrange(self.frame_count))]
        i = 0

    def get_frame(self):
        global i
        if i < self.frame_count:
            i += 1
            sleep(0.04)
            return self.frames[i]
        else:
            i = 0