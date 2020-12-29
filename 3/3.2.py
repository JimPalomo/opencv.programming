# Resize Image

import cv2 as cv
import numpy as np

img = cv.imread("../Resources/car.jpg")
print(img.shape)    # results: (height, width, channel (bgr))

imgResize = cv.resize(img, (800, 500))  # resize(image, (width, height))
print(imgResize.shape)                  # results: (height, width, channel (bgr))

imgCropped = img[0:500, 300:800]        # [height, width]

cv.imshow("Original", img)              # original
cv.imshow("Resized", imgResize)         # resized
cv.imshow("Cropped", imgCropped)

cv.waitKey(0)
cv.destroyAllWindows()  # close all windows