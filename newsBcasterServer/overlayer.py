from cv2 import putText
from cv2 import FONT_ITALIC
from math import floor, ceil

width, height = (0, 0)


def getwandh(wt, ht):
    global width, height
    width = wt
    height = ht


def pixrange(m, n):
    i = m
    while i < n:
        yield i
        i += 1


def overlay(frame, frame_num, overlay_text="Headlines Go HERE", bgcolor=200):
    """
    :type overlay_text: string
    :type frame_num: int
    :type frame: OpenCV Video Frame
    """
    text_speed_factor = frame_num * 2
    for i in pixrange(int(floor(height * 0.9)), height):
        for k in pixrange(0, width):
            frame[i, k] = [bgcolor]
    font = FONT_ITALIC
    # if len(overlay_text)%width is not 0:
    if frame_num >= width:
        frame_num = 0
    putText(frame, overlay_text, (int(ceil(width * 0.9)) - text_speed_factor, int(height * .99) - 1), font, 0.5, (0),
            1)
    return frame
