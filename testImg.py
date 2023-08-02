import cv2



cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)
    c = cv2.waitKey(0)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()

# import numpy as np
# import cv2
# cap = cv2.VideoCapture(0)
# while cap.isOpened():
#     flags, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('img', gray)
#     key = cv2.waitKey(0) & 0xFF
#     if key == ord("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()
