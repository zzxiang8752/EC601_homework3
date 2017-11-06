#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 00:04:23 2017

@author: zhongzhengxiang
"""

import cv2
import numpy as np  
#Load an image
img = cv2.imread('Lenna.png')
# Convert the image to Gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

threshold_type = 2
threshold_value = 128
retval,dst = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_TRUNC)

cv2.namedWindow("Original Image")
cv2.imshow("Original Image", img)


cv2.namedWindow("Thresholded Image")
cv2.imshow("Thresholded Image",dst)


current_threshold = 128
max_threshold = 255

# Threshold type: Binary
retval2,threshold = cv2.threshold(gray, current_threshold, max_threshold, cv2.THRESH_BINARY)

cv2.namedWindow("Binary threshold")
cv2.imshow("Binary threshold",threshold)
cv2.imwrite("Binary threshold.jpg",threshold)

# Band thresholding
threshold1 = 27
threshold2 = 125
retval3, binary_image1 = cv2.threshold(gray, threshold1, max_threshold, cv2.THRESH_BINARY)
retval4, binary_image2 = cv2.threshold(gray, threshold1, max_threshold, cv2.THRESH_BINARY_INV)
band_thresholded_image = np.bitwise_and(binary_image1, binary_image2)

cv2.namedWindow("Band Thresholding")
cv2.imshow("Band Thresholding",band_thresholded_image )
cv2.imwrite("Band Thresholding.jpg",band_thresholded_image )

#Semi thresholding
retval5,semi_thresholded_image = cv2.threshold(gray, current_threshold, max_threshold, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
semi_thresholded_image = np.bitwise_and( gray, semi_thresholded_image)

cv2.namedWindow("Semi Thresholding")
cv2.imshow("Semi Thresholding",semi_thresholded_image )
cv2.imwrite("Semi Thresholding.jpg",semi_thresholded_image )

#Adaptive thresholding
adaptive_thresh = cv2.adaptiveThreshold(gray, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 10 )
cv2.namedWindow("Adaptive Thresholding")
cv2.imshow("Adaptive Thresholding",adaptive_thresh)
cv2.imwrite("Adaptive Thresholding.jpg",adaptive_thresh)

cv2.waitKey(0)