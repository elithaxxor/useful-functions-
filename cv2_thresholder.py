# import the necessary packages
import argparse
import cv2

'''
:: SAMPLE BASIC THRESHOLDING :: 
1. CONVERT TO GREYSCALE
2. APPLY 7X7 GAUSSIAN BLUR 
3. APPLY THRESHILD
## FIRST PARAMETER IS IMAGE, 2ND IS 'THRESHOLD CHECK' 
## IF PIXLE IS GREATER THAN 200, SET TO BLACK 
## ELSE SET IT TO WHITE 
'''

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
(T, threshInv) = cv2.threshold(blurred, 200, 255,
	cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)
(T, threshInv) = cv2.threshold(blurred, 200, 255,
	cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)



