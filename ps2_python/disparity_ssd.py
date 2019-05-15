import numpy as np
import cv2
from numpy.lib.stride_tricks import as_strided

def sumsqdiff2(input_image, template, valid_mask=None):
    '''
    ssd implementation borrowed from:
        http://stackoverflow.com/questions/17881489/faster-way-to-calculate-sum-of-squared-difference-between-an-image-m-n-and-a
    '''
    pass


def disparity_ssd(L, R, block_size=5, disparity_range=30, lambda_factor=0):
    """Compute disparity map D(y, x) such that: L(y, x) = R(y, x + D(y, x))

    Params:
    L: Grayscale left image
    R: Grayscale right image, same size as L

    Returns: Disparity map, same size as L, R
    """
    pass

