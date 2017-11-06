#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 21:53:11 2017

@author: zhongzhengxiang
"""

import cv2

filename = "baboon.jpg"

src = cv2.imread(filename,cv2.IMREAD_COLOR)
b,g,r = cv2.split(src)
cv2.imshow("Original image",src)
cv2.imshow("Red",r)
#cv2.imwrite("output_ex2/Red.jpg",r)
cv2.imshow("Green",g)
cv2.imshow("Blue",b)
print('value at R(20,25):',r[20][25])
print('value at G(20,25):',g[20][25])
print('value at B(20,25):',b[20][25])

ycrcb_image = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
y,cb,cr = cv2.split(ycrcb_image)
cv2.imshow("Y",y)
cv2.imshow("Cb",cb)
cv2.imshow("Cr",cr)
print('value at Y(20,25):',y[20][25])
print('value at Cb(20,25):',cb[20][25])
print('value at Cr(20,25):',cr[20][25])

hsv_image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv_image)
cv2.imshow("Hue",h)
cv2.imshow("Saturation",s)
cv2.imshow("Value",v)   
print('value at H(20,25):',h[20][25])
print('value at S(20,25):',s[20][25])
print('value at V(20,25):',v[20][25])
    
cv2.waitKey(0)
cv2.destroyAllWindows() ## Destroy all windows

