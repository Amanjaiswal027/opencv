import cv2
import numpy as np

# Start capturing video from the default camera (usually the webcam)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break  # Exit the loop if the frame is not captured correctly

    width = int(cap.get(3))  # Get the width of the video frame
    height = int(cap.get(4))  # Get the height of the video frame

    # Convert the frame from BGR (default in OpenCV) to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Create a binary mask where blue colors are white and the rest are black
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Bitwise-AND the original frame with the mask to extract the blue regions
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the resulting frame showing only the blue areas
    cv2.imshow('frame', result)

    # Display the mask showing where the blue areas are
    cv2.imshow('mask', mask)

    # Break the loop and exit if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
