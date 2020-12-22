# Display image

import cv2 as cv

img = cv.imread("car.jpg")

cv.imshow("Output", img)
cv.waitKey(0)