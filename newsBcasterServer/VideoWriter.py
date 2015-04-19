import cv2

global i

class VideoWriter:
    def __init__(self, vid_fps, vid_width, vid_height, filename="out", vid_format="mov"):
        global i
        self.fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')

        self.out = cv2.VideoWriter(filename + '.' + vid_format, self.fourcc, float(vid_fps),
                                   (int(float(vid_width)), int(float(vid_height))))
        i = 0

    def writer(self, frame):
        global i
        cv2.imwrite("out/" + str(i) + ".jpg", frame)
        i += 1
        self.out.write(frame)
