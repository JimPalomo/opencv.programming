# Grayscale image

import cv2 as cv

img = cv.imread("../Resources/car.jpg")

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Grayscale", imgGray)
cv.waitKey(0)