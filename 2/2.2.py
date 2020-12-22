import cv2 as cv

img = cv.imread("../Resources/car.jpg")

imgBlur = cv.GaussianBlur(img, (7,7), 0)

cv.imshow("Grayscale", imgBlur)
cv.waitKey(0)