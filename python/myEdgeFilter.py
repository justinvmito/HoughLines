import matplotlib.pyplot as plt
import math
import numpy as np
import cv2
from scipy.signal.windows import gaussian    # For signal.gaussian function
from myImageFilter import myImageFilter
from myNMS import myNMSDirectional

def myEdgeFilter(img0, sigma):
    # YOUR CODE HERE
   
    hsize = 2 * math.ceil(3*sigma) + 1
    separate = gaussian(hsize, sigma)
    kernel = np.outer(separate, separate)

    # img1 refers to img0 after being convolved by the gaussian smoothing kernel
    img1 = myImageFilter(img0, kernel)

    # imgx refers to img1's gradient in the x direction
    xSobel = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
    imgx = myImageFilter(img1, xSobel)
    ySobel = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
    imgy = myImageFilter(img1, ySobel)

    # Produce the edge magnitude image
    img1 = np.sqrt(np.add(np.power(imgx, 2), np.power(imgy, 2)))
    # Get angles
    angles = np.arctan2(imgy, imgx)
    angles = cv2.dilate(angles, np.ones((3, 3)), iterations = 1)
    # Call NMS function
    return myNMSDirectional(angles, img1)
