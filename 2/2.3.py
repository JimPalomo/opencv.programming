# Canny image (draw edges)

import cv2 as cv

img = cv.imread("../Resources/car.jpg")

# imgCanny = cv.Canny(img, 100, 100)
imgCanny = cv.Canny(img, 150, 200)  # less edges

cv.imshow("Canny", imgCanny)
cv.waitKey(0)