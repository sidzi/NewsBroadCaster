import cv2

import overlayer


class videoWriter:
    def __init__(self, vid_fps, vid_width, vid_height, filename="out", vid_format="mov"):
        self.fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')

        self.out = cv2.VideoWriter(filename + '.' + vid_format, self.fourcc, float(vid_fps),
                                   (int(float(vid_width)), int(float(vid_height))))

    def writer(self, frame):
        frame = overlayer.overlay(frame)
        self.out.write(frame)
