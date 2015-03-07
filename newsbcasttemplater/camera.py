import cv2


class Camera(object):
    def __init__(self):
        cap = cv2.VideoCapture('lmao.mp4')
        while True:
            ret, self.frames = cap.read()
        cap.release()
        cv2.destroyAllWindows()

    def get_frame(self):
        return self.frames


