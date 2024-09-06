import cv2

# Read the image from the specified path
img = cv2.imread('asset\logo1.png', 0)

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Resize the image to half its original size
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    
    # Rotate the image 90 degrees clockwise
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    
    # Display the image in a window
    cv2.imshow('image', img)
    
    # Wait for a key press indefinitely
    cv2.waitKey(0)
    
    # Destroy all OpenCV windows
    cv2.destroyAllWindows()
