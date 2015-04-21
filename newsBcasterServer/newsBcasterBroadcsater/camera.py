from time import sleep

global i


class Camera(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self):
        global i
        self.frames = [open("out/" + str(f) + '.jpg', 'rb').read() for f in list(xrange(200))]
        i = 0

    def get_frame(self):
        global i
        if i < 198:
            i += 1
            sleep(0.04)
            return self.frames[i]
        else:
            i = 0