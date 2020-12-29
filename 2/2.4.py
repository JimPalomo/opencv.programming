# Dilation image (make edges thicker)

import cv2 as cv
import numpy as np

img = cv.imread("../Resources/car.jpg")
kernel = np.ones((5,5), np.uint8)   # ones(matrix 5x5, declare unsigned integers 8 bit [0-255])

imgCanny = cv.Canny(img, 150, 200)  
imgDialation = cv.dilate(imgCanny, kernel, iterations = 1)  # iterations -> edge thickness (adds extra pixels to the edges)

cv.imshow("Dilation", imgDialation)
cv.waitKey(0)