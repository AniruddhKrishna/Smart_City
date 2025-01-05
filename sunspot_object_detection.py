 import cv2
       
 # Load the image
 image = cv2.imread('July_spots.jpg')
 # Convert the image to grayscale
 #Converting images to grayscale simplifies processing by reducing color
 #complexity to a single channel of intensity values
 gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 # Apply Gaussian blur with a kernel size of (5, 5)
 #blurs out the whole image and brings an evenness to the image by reducing noise ( reducing frequency)
 blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
 # Apply adaptive thresholding to detect dark regions
 #We are setting a threshold by mapping all values more than the mean as 255 and below as 0
 #cv2.ADAPTIVE_THRESH_MEAN_C calculates men , the size around the pixel is 11x11 for calculating the threshold
 #cv2.THRESH_BINARY_INV does the classification
 # 10 is just a constant we subtract from the mean
 binary_image = cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11,10)
 # Find contours in the dilated binary image
 # cv2.RETR_LIST retrieves all contours
 #cv2.CHAIN_APPROX_SIMPLE saves all contours
 contours, _ = cv2.findContours(binary_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
 # Draw contours on a copy of the original image
 image_with_contours = image.copy()
 # Iterate through contours
 for i, contour in enumerate(contours):
     cv2.drawContours(image_with_contours, contours, i, (0, 255, 0), thickness=1) # Draw contour in green
 # Show the image with contours
 cv2.imshow('Image with Contours around Dark Spots', image_with_contours)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
