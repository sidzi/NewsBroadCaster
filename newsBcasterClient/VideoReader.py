import cv2


class videoReader:
    def __init__(self, filepath):
        # noinspection PyArgumentList
        self.cap = cv2.VideoCapture(filepath)
        self.frame_count = str(self.cap.get(7))
        self.frame_width = str(self.cap.get(3))
        self.frame_height = str(self.cap.get(4))
        self.frames_per_sec = str(self.cap.get(5))

    def getcap(self):
        return self.cap

    def close(self):
        self.cap.release()

