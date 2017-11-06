# EC601_homework3

# Exercise 1

In ColorImage.cpp, cvMat is a matrix which store the pixels of the image. It has three channels, red, green and blue. Matrix elements are stored row by row. Programs read cvMat object by using cvMatName.at(x,y). Program read the cvMat object in a similar way with the matrix object.

# Exercise 2
There are three types to construct the picture. Each types have three channels,each picture show each channel of each types.

('value at R(20,25):', 153)
('value at G(20,25):', 215)
('value at B(20,25):', 252)
('value at Y(20,25):', 201)
('value at Cb(20,25):', 94)
('value at Cr(20,25):', 157)
('value at H(20,25):', 101)
('value at S(20,25):', 100)
('value at V(20,25):', 252)

value range of R,G,B is 0~255.

value range of Y,U,V is 16~235 and 16~240 and 16~240

value range of H,S,V is 0~180 and 0~255 and 0~255

value range of L,A,B is 0~100,-127~127,-127~127

value range of C,M,Y,K  is 0~100 

# Exercise 3

2.In this exercise,the program use one set of parameters to represent the result.This exercise first add noise into picture,there are two types of noise, gaussian noise and salt-pepper noise. Gaussian filter works better for Gaussiannoise images and median filter works better for Salt-and-pepper images.With the increase of kernel size, the image becomes less clear.

# Exercise4

2.What are the disadvantages of binary threshold?

Binary threshold convert all images into black and white,because it set the threhold to divide the different color into two kinds of colors,so that there are no more other colors,loss the diversity.

3.When is Adaptive Threshold useful?

Adaptive Threshold can choose the better threshold for each picture,so that each picture can have it's own best threshold.
