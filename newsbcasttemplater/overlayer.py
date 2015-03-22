import cv2


def overlay(frame, text="Enter text"):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, (10, 300), font, 4, (255, 255, 255), 2)
    return frame
