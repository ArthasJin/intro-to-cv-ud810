#!/usr/bin/env python

import cv2
import numpy as np
import os.path

'''
Problem Set 0: Images as Functions
'''

if __name__ == '__main__':
    img1 = cv2.imread('input/lena.jpg', cv2.IMREAD_COLOR)
    img2 = cv2.imread('input/woman.tiff', cv2.IMREAD_COLOR)

    # Problem 2: Produce monochrome images using their channels
    img1_copy = np.copy(img1)
    img1[:,:,0], img1[:,:,2] = img1[:,:,2], img1[:,:,0]
    img1_green = img1_copy[:,:,1]
    img1_red = img1_copy[:,:,0]
    img1_blue = img1_copy[:,:,2]
    img1_greater = img1_green > img1_red

    # Problem 3: crop a 100x100 center region from mono img2 and paste in mono img1
    img1_greyscale = cv2.imread('input/lena.jpg', cv2.IMREAD_GRAYSCALE)
    img2_greyscale = cv2.imread('input/woman.tiff', cv2.IMREAD_GRAYSCALE)
    shape1 = img1_greyscale.shape
    shape2 = img2_greyscale.shape
    crop = img1_greyscale[shape1[0]/2-50:shape1[0]/2+50, shape1[1]/2-50:shape1[1]/2+50]
    img2_greyscale[shape2[0]/2-50:shape2[0]/2+50, shape2[1]/2-50:shape2[1]/2+50] = crop
    
    # Problem 4:
    # a) Min and Max values of green image
    min_value = np.min(img1_green)
    max_value = np.max(img1_green)
    mean_value = np.mean(img1_green)
    std_value = np.std(img1_green)
    print("min = {}, max = {}, mean = {}, std = {}".format(min_value, max_value, mean_value, std_value))

    # b) normalize img1_green and then multiply with 10 and add the mean
    img_normalize = cv2.add(cv2.multiply(cv2.divide(cv2.subtract(img1_green, mean_value), std_value), 10), mean_value)

    cv2.imshow('normalize', img_normalize)
    img_normalize_copy = np.copy(img_normalize)

    # c) shift img by 2 pixels to the left
    cv2.imshow('shifted', img_normalize[:,2:-1])
    # cv2.warpAffine(img_normalize_copy, )

    # d) subtract shifted version from original
    # cv2.imshow('subtract', img_normalize - img_normalize[:,2:-1])

    # Problem 5: Gaussian Noise Addition
    # a) add Gaussian noise to green channel

    img1_green_copy = np.copy(img1)
    width, height, depth = img1_green_copy.shape
    noise = np.zeros((width, height), np.uint8)
    cv2.randn(noise, 0, 30)
    cv2.imshow('gaussian green', img1_green_copy[:,:,1] + noise)

    # b) add Gaussian noise to the blue channel
    cv2.imshow('gaussian blue', img1_green_copy[:,:,0] + noise)

    cv2.waitKey()

    '''
    The same gaussian noise is more visible in the green channel than the blue,
    due to the increased sensitivity of the eye to the green color spectrum
    '''
