# ---------------------------------------------------------
# Name : Wijerathna W.M.M.T.
# Reg No: EG/2020/4291
# Take Home Assignment 1
# Question 2
# ---------------------------------------------------------
import cv2
import numpy as np

# Read the original image
image = cv2.imread('D:/Academic/7th _sem/COM_VISION/Take_Home_1/data/sample.jpg')

# Name the windows
window_names = ['Original Image', '3x3 Blur', '10x10 Blur', '20x20 Blur']

# Create windows with a set size
for window in window_names:
    cv2.namedWindow(window, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window, 640, 480)

# This function applies a 3x3 blur
def average_3x3():
    blurred = cv2.blur(image, (3, 3))
    cv2.imshow(window_names[1], blurred)

# This function applies a 10x10 blur
def average_10x10():
    blurred = cv2.blur(image, (10, 10))
    cv2.imshow(window_names[2], blurred)

# This function applies a 20x20 blur
def average_20x20():
    blurred = cv2.blur(image, (20, 20))
    cv2.imshow(window_names[3], blurred)

# Show the original image
cv2.imshow(window_names[0], image)

# Apply the blurs and show them
average_3x3()
average_10x10()
average_20x20()

# Wait for any key press, then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
