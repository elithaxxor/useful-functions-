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

### CV2 DILATE 
'''
cv2 dilate can only take binary, used to exoand/contract foreground boundries.

Image dilation is helpful because if you have performed erosion, then erosion already removed the white noises, but it also contracts our object. 
So we dilate it. Since the noise is gone, they won’t come back, but our object area increases. Dilation is useful in joining broken parts of an object.

'''
import numpy as np
import cv2

img = cv2.imread('data.png', 1)
cv2.imshow('Original', img)

kernel = np.ones((5, 5), 'uint8')
dilate_img = cv2.dilate(img, kernel, iterations=1)
cv2.imshow('Dilated Image', dilate_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Use cv2 find countour to find countours (contiounous lines) - best used with binary images 

'''
import numpy as np
import cv2 as cv
im = cv.imread('test.jpg')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


