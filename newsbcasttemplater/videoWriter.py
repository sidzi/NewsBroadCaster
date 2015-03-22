import cv2


class videoWriter:
    def __init__(self):
        self.fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')

    def write(self, vid_fps, vid_width, vid_height, filename="out", vid_format="mov"):
        out = cv2.VideoWriter(filename + '.' + vid_format, self.fourcc, float(vid_fps),
                              (int(float(vid_width)), int(float(vid_height))))
