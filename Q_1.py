# ---------------------------------------------------------
# Name : Wijerathna W.M.M.T.
# Reg No: EG/2020/4291
# Take Home Assignment 1
# Question 1
# ---------------------------------------------------------
import cv2
import numpy as np

# Read the image in gray mode
image = cv2.imread('D:/Academic/7th _sem/COM_VISION/Take_Home_1/data/sample.jpg', cv2.IMREAD_GRAYSCALE)

# Make a window to show the image
window_name = 'Intensity Adjustment'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 640, 480)

# Set the trackbar range
max_intensity = 8
initial_intensity = 3
current_intensity = initial_intensity

# This function is called when the trackbar is changed
def update_intensity(value):
    global current_intensity
    current_intensity = 2 ** (8 - value)

    # Reduce the image by dividing its pixel values
    img_reduced = np.uint8(np.floor(np.double(image) / (current_intensity)))

    # Make the new image fit between 0 and 255
    updated_image = cv2.normalize(img_reduced, None, 0, 255, norm_type=cv2.NORM_MINMAX)

    # Show the updated image
    cv2.imshow(window_name, updated_image)

# Add a trackbar to the window
cv2.createTrackbar('Intensity', window_name, initial_intensity, max_intensity, update_intensity)

# Show the original image
cv2.imshow(window_name, image)

# Wait for any key to be pressed, then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
# ---------------------------------------------------------
# Name : Wijerathna W.M.M.T.
# Reg No: EG/2020/4291
# Take Home Assignment 1
# Question 1
# ---------------------------------------------------------
import cv2
import numpy as np

# Read the image in gray mode
image = cv2.imread('data/sample.jpg', cv2.IMREAD_GRAYSCALE)

# Make a window to show the image
window_name = 'Intensity Adjustment'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 640, 480)

# Set the trackbar range
max_intensity = 8
initial_intensity = 3
current_intensity = initial_intensity

# This function is called when the trackbar is changed
def update_intensity(value):
    global current_intensity
    current_intensity = 2 ** (8 - value)

    # Reduce the image by dividing its pixel values
    img_reduced = np.uint8(np.floor(np.double(image) / (current_intensity)))

    # Make the new image fit between 0 and 255
    updated_image = cv2.normalize(img_reduced, None, 0, 255, norm_type=cv2.NORM_MINMAX)

    # Show the updated image
    cv2.imshow(window_name, updated_image)

# Add a trackbar to the window
cv2.createTrackbar('Intensity', window_name, initial_intensity, max_intensity, update_intensity)

# Show the original image
cv2.imshow(window_name, image)

# Wait for any key to be pressed, then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
