import cv2
video=cv2.VideoCapture(0)
while True:
    ret,Frame=video.read()
    cv2.imshow("frame",Frame)
    if cv2.waitKey(1) and 0xFF ==ord('q'):
        break
video.release()
cv2.destroyAllWindows