 import cv2
# Load the image
image = cv2. imread ( 'water_body-jpg') # Replace 'water_body jpg' with the path to your image.
# Convert the image to grayscale
# Converting the image to grayscale simplifies processing by reducing it to a single intensity channel.
gray_image = cv2. cvtColor (image, cv2. COLOR_BGR2GRAY)
# Apply Gaussian blur with a kernel size of (5, 5)
# Blurring helps in reducing noise and smoothening the image for better thresholding.
blurred_image = cv2. GaussianBlur (gray_image, (5, 5), 0)
# Apply adaptive thresholding to detect spots
# Adaptive thresholding is used to highlight regions that deviate in intensity.
binary_image = cv2.adaptiveThreshold (blurred_image, 255, cv2. ADAPTIVE_THRESH_MEAN_C, Cv2. THRESH_BINARY_INV, 11, 10)
# Dilate the binary image to enhance the visibility of small spots
# Dilation helps to emphasize the features of the detected spots.
dilated_image = cv2. dilate(binary_image, None, iterations=2)
# Find contours in the binary image
# This step identifies the boundaries of the detected spots.
contours, _ = cv2. findContours(dilated_image, cv2. RETR_LIST, cv2. CHAIN_APPROX_SIMPLE)
# Draw contours on a copy of the original image
image_with_contours = image.copy()
# Iterate through contours and draw them on the image
for i, contour in enumerate (contours):
    area = cv2. contourArea (contour)
if area > 50: # Adjust the threshold area based on the size of spots you want to detect cv2. drawContours (image_with_contours, contours, i, (0, 255, 0), thickness=2)
# Draw contours in green
# Show the image with contours
cv2.imshow('Spots Detected in Water Body', image_with_contours)
cv2.waitKey (0)
cv2.destroyAllWindows ()
