import random
import cv2

# Load the image
img = cv2.imread('assets/logo1.jpg', -1)

tag = img[500:700 , 600:900]
img[100:300, 650:950] = tag
#this is how we can cut the image and paste it anywhere

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Print the color of the pixel at position (257, 400)
    # Ensure the indices are within bounds
    
    for i in range(100):
        if i < img.shape[0]:  # Ensure we don't go out of bounds
            for j in range(img.shape[1]):
                img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        else:
            break  # Stop if the image has fewer than 100 rows

    # Display the modified image
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
