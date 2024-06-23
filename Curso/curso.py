import cv2 as cv
img = cv.imread("C:\\Users\\User\\Desktop\\Info 2\\EXTRA\\fondos\\834017.png")

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window