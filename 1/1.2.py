# Display Video

import cv2 as cv

cap = cv.VideoCapture("../Resources/traffic.mp4")

while True:
    success, img = cap.read()
    cv.imshow("Video", img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break