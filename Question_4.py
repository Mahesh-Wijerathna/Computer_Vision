# ---------------------------------------------------------
# Name : Wijerathna W.M.M.T.
# Reg No: EG/2020/4291
# Take Home Assignment 1 
# Question 4
# ---------------------------------------------------------
import cv2
import numpy as np

# Read the original image
image = cv2.imread('D:/Academic/7th _sem/COM_VISION/Take_Home_1/data/sample.jpg', cv2.IMREAD_COLOR)

# List of block sizes
block_sizes = [3, 5, 7]

# Function to make a block-averaged version of an image
def process_image(image, block_size):
    result = np.copy(image)

    # Loop through the image in steps of block_size
    for y in range(0, image.shape[0], block_size):
        for x in range(0, image.shape[1], block_size):
            # Get the block area
            block = image[y:y + block_size, x:x + block_size]
            # Find the average color of the block
            mean_color = np.mean(block, axis=(0, 1))
            # Fill the block area with the average color
            result[y:y + block_size, x:x + block_size] = mean_color

    return result

# Create processed images for each block size
processed_images = [process_image(image, size) for size in block_sizes]

# Show the original image
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original Image', 640, 480)
cv2.imshow('Original Image', image)

# Show processed images
for i, processed_image in enumerate(processed_images):
    window_name = f'Block {block_sizes[i]}x{block_sizes[i]}'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 640, 480)
    cv2.imshow(window_name, processed_image
