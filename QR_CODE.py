import cv2
import pyzbar.pyzbar as pyzbar
import numpy as np

cap = cv2.VideoCapture(0)
string = ""
while(True):
    ret, frame = cap.read()
    cv2.imshow("frame",frame)
    qr_code = pyzbar.decode(frame)
    for word in qr_code:
        print(word.data)

    if(cv2.waitKey(1) == 13):
        break


