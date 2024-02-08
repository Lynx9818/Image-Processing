import cv2 

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    cv2.imshow("Video", frame)
    k = cv2.waitKey(1)&0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
