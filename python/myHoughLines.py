import numpy as np
import cv2
from myNMS import myNMS
def myHoughLines(H, nLines):
    # YOUR CODE HERE
    result = myNMS(nLines, H)
    return [result[0].astype(int), result[1].astype(int)]



