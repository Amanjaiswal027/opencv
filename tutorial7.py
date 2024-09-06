import numpy as np
import cv2

# Load the main image and template
img = cv2.imread(r'asset\soccer_practice.jpg')
template = cv2.imread(r'asset\ball.PNG')

# Convert both images to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Get the dimensions of the template
h, w = template_gray.shape[:2]

# Define the matching methods
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF_NORMED]

# Loop over all matching methods
for method in methods:
    img2 = img_gray.copy()

    # Perform template matching
    result = cv2.matchTemplate(img2, template_gray, method)

    # Get the minimum and maximum values and their locations in the result
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Determine the top-left corner based on the matching method
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc  # For these methods, the minimum location is the best match
    else:
        top_left = max_loc  # For other methods, the maximum location is the best match

    # Draw a rectangle around the detected template
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 2)

    # Display the result
    cv2.imshow('Matching Result', img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
