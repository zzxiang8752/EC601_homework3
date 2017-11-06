#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 23:02:32 2017

@author: zhongzhengxiang
"""

import cv2
import numpy as np 


def Add_gaussian_Noise(img,mean,sigma):
    noiseArr = img.copy()
    noiseArr = np.random.normal(mean,sigma,img.shape)
    np.add(img,noiseArr,img,casting="unsafe")

def Add_salt_pepper_Noise(img,pa,pb):
    row,col,ch=img.shape
    #Controls the amount of black spots in the noise
    amount1=row*col*pa
    #Controls the amount of white spots in the noise    
    amount2=row*col*pb
    for i in range(int(amount1)):
        img[int(np.random.uniform(0,row))][int(np.random.uniform(0,col))]=0
    for i in range(int(amount2)):
        img[int(np.random.uniform(0,row))][int(np.random.uniform(0,col))]=255

def main():

    img=cv2.imread('Lenna.png')
    cv2.namedWindow('Original image')
    cv2.imshow('Original',img)
    cv2.imwrite('Original.jpg',img)

#gaussian_Noise
    noise_img=img.copy()
    mean=20
    sigma=100
    Add_gaussian_Noise(noise_img,mean,sigma)
    cv2.imshow('Gaussian Noise',noise_img)
    cv2.imwrite('Gaussian_Noise.jpg',noise_img)

    noise_dst=noise_img.copy()
    cv2.blur(noise_dst,(3,3))
    cv2.imshow('Box filter',noise_dst)
    cv2.imwrite('Box_filter.jpg',noise_dst)

    noise_dst1=noise_img.copy()
    cv2.GaussianBlur(noise_dst1,(3,3),1.5)
    cv2.imshow('GaussianBlur filter',noise_dst1)
    cv2.imwrite('GaussianBlur filter.jpg',noise_dst1)
    

    noise_dst2=noise_img.copy()
    cv2.medianBlur(noise_dst2,3)
    cv2.imshow('Median filter',noise_dst2)
    cv2.imwrite('Median filter.jpg',noise_dst2)
    


#salt_pepper_Noise
    noise_img2=img.copy()
    pa=0.4
    pb=0.4
    Add_salt_pepper_Noise(noise_img2,pa,pb)
    cv2.imshow("Salt and Peper Noise", noise_img2)
    cv2.imwrite("Salt and Peper Noise.jpg", noise_img2)
    
    noise_dst3=noise_img2.copy()
    cv2.blur(noise_dst3,(3,3))
    cv2.imshow('Box filter2',noise_dst3)
    cv2.imwrite('Box filter2.jpg',noise_dst3)
    

    noise_dst4=noise_img2.copy()
    cv2.GaussianBlur(noise_dst4,(3,3),1.5)
    cv2.imshow('GaussianBlur filter2',noise_dst4)
    cv2.imwrite('GaussianBlur filter2.jpg',noise_dst4)
    

    noise_dst5=noise_img2.copy()
    cv2.medianBlur(noise_dst5,3)
    cv2.imshow('Medianfilter2',noise_dst5)
    cv2.imwrite('Medianfilter2.jpg',noise_dst5)
    
    
    print('mean:',mean)
    print('sigma:',sigma)
    print('pa:',pa)
    print('pb:',pb)
    print('best kernel size: 3x3')
   
    cv2.waitKey(0)


if __name__ == "__main__":
    main()