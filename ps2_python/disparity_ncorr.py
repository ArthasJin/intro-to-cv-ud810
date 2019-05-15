import numpy as np
import cv2

def disparity_ncorr(L, R, block_size=5, disparity_range=30, lambda_factor=0):
    """Compute disparity map D(y, x) such that: L(y, x) = R(y, x + D(y, x))

    Params:
    L: Grayscale left image
    R: Grayscale right image, same size as L

    Returns: Disparity map, same size as L, R
    """
    pass

