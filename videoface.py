import time

import cv2
import pandas as pandas

first_frame=None
status_list=[None,None]


video=cv2.VideoCapture(0)

while True:

    check,frame=video.read()
    status=0

    print(check)
    print(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue

    cv2.imshow("capturing",gray)
    key=cv2.waitKey(1)
    if key ==ord('q'):
        break



video.release()