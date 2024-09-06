import numpy as np
import cv2

# Load the image, using raw string for the file path
img = cv2.imread(r'asset\chessboard.png')

# Check if the image is loaded successfully
if img is None:
    print("Error: Image not found or unable to load.")
    exit()

# Convert to grayscale for corner detection
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect corners using the Shi-Tomasi corner detection method
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

# Convert corners to integer values
corners = np.int0(corners)

# Draw circles around detected corners
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

# Draw lines connecting corners
for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])  # Convert to tuple for point1
        corner2 = tuple(corners[j][0])  # Convert to tuple for point2
        color = tuple(np.random.randint(0, 255, size=3).tolist())  # Random color for each line
        cv2.line(img, corner1, corner2, color, 1)

# Display the final image with corners and lines
cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
