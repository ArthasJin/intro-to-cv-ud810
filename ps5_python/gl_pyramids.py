import cv2
import numpy as np

def laplacian_pyramid(img, levels):
    pass

def gaussian_pyramid(img, levels):
    pass

def reduce(img):
    #  g = cv2.blur(img, (5,5))[::2, ::2]
    #  g = cv2.GaussianBlur(img, (3,3), 0)[::2, ::2]
    pass

def expand(img):
    #  new_shape = (img.shape[1] * 2, img.shape[0] * 2)
    #  return cv2.GaussianBlur(cv2.resize(img, new_shape), (3,3), 0, cv2.INTER_AREA)
    pass
