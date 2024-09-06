import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    width = int(cap.get(3))
    height = int(cap.get(4))

    # Create a blank image with the same shape as the frame
    image = np.zeros(frame.shape, np.uint8)

    # Resize the frame to half its size
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Place the smaller frame in the four quadrants of the image
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # top_left
    image[height//2:, :width//2] = smaller_frame   # bottom_left
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # top_right
    image[height//2:, width//2:] = smaller_frame   # bottom_right

    # Display the image
    cv2.imshow('frame', image)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
