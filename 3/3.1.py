# Resize Image

import cv2 as cv

img = cv.imread("../Resources/car.jpg")
print(img.shape)    # results: (height, width, channel (bgr))

imgResize = cv.resize(img, (800, 500))  # resize(image, (width, height))
print(imgResize.shape)                  # results: (height, width, channel (bgr))

cv.imshow("Image", img)             # original
cv.imshow("Resized", imgResize)     # resized

cv.waitKey(0)
cv.destroyAllWindows()  # close all windows