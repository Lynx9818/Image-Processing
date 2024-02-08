import cv2

img = cv2.imread("C:\\Users\\levanlinh\\OneDrive - lynxxx\\Photos\\halongbay.jpg", 1)
img_sz = cv2.resize(img, None, fx = 0.2, fy = 0.2)

cv2.imshow("Image", img_sz)
cv2.waitKey(0)
cv2.destroyAllWindows()
