import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    img = np.zeros(frame.shape, np.uint8)
    width = int(capture.get(3))
    height = int(capture.get(4))
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    img[:height // 2, :width // 2] = small_frame
    img[:height // 2, width // 2:] = cv2.rotate(small_frame, cv2.cv2.ROTATE_180)
    img[height // 2:, :width // 2] = cv2.rotate(small_frame, cv2.cv2.ROTATE_180)
    img[height // 2:, width // 2:] = small_frame
    #img[100, 200] = img[220, 320]
    cv2.imshow('frame', img)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()


