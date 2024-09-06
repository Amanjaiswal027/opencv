import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    width = int(cap.get(3))
    height = int(cap.get(4))

    # Draw a blue rectangle on the frame
    cv2.rectangle(frame, (0, 0), (width, height), (255, 0, 0), 10)
    # (0, 0) is the starting position (top-left corner)
    # (width, height) is the ending position (bottom-right corner)
    # (255, 0, 0) is the color (BGR format: blue in this case)
    # 10 is the thickness of the rectangle border

    # Display the frame with the rectangle
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()  # Added parentheses to correctly call the release method
cv2.destroyAllWindows()