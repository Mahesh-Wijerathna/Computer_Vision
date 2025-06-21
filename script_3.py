# ---------------------------------------------------------
# Name : Wijerathna W.M.M.T.
# Reg No: EG/2020/4291
# Take Home Assignment 1
# Question 3
# ---------------------------------------------------------
import cv2

# Read the original image
image = cv2.imread('D:/Academic/7th _sem/COM_VISION/Take_Home_1/data/sample.jpg')

# Get the image size
rows, cols = image.shape[:2]

# Create a rotation matrix for 45° clockwise
rotation_matrix_45 = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1.0)
rotated_image_45 = cv2.warpAffine(image, rotation_matrix_45, (cols, rows))

# Create a rotation matrix for 90° clockwise
rotation_matrix_90 = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1.0)
rotated_image_90 = cv2.warpAffine(image, rotation_matrix_90, (cols, rows))

# List of window names
windows = ['Original Image', 'Image Rotated 45°', 'Image Rotated 90°']

# Create windows for showing the images
for window in windows:
    cv2.namedWindow(window, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window, 640, 480)

# Show the images
cv2.imshow(windows[0], image)
cv2.imshow(windows[1], rotated_image_45)
cv2.imshow(windows[2], rotated_image_90)

# Wait until a key is pressed, then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
