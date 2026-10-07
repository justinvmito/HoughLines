import numpy as np
import math

from myEdgeFilter import myEdgeFilter

def myHoughTransform(Im, rhoRes, thetaRes):
    # YOUR CODE HERE
    # The row index represents p
    numRows = int(math.sqrt(math.pow(Im.shape[0], 2) + math.pow(Im.shape[1], 2)) / rhoRes)
    # the column index represents the angle
    numCols = int(2*math.pi / thetaRes)
    # img_hough is the accumulator. The + 1 to the size allows for 0 to refer to value 0, and 400 to refer to 400
    img_hough = np.zeros((numRows + 1, numCols + 1))
    for i, x in np.ndenumerate(Im):
        if x != 0:
            for angle in np.arange(numCols):
                # Convert from index to angle
                theta = angle * thetaRes
                rho = i[1] * math.cos(theta) + i[0] * math.sin(theta)
                if rho >= 0 and rho <= numRows * rhoRes:
                    # convert from angle and rho back to index
                    theta = int(theta / thetaRes)
                    rho = int(rho / rhoRes)
                    img_hough[rho, theta] += 1
    thetaScale = np.array([])
    for theta in np.arange(img_hough.shape[1]):
        # If this value of theta is unused, then the unique_counts would be 1.
        # In the case that all combinations of rho and this theta have the same # of votes, 
        # then if the # of votes isn't 0, then we know that this theta was used.
        if np.unique_counts(img_hough[:,theta] > 1) or not 0 in img_hough[:,theta]  :
            thetaScale = np.append(thetaScale, theta * thetaRes)
    rhoScale = np.array([])
    for rho in np.arange(img_hough.shape[0]):
        # uses the same logic as above for theta
        if np.unique_counts(img_hough[rho, :]> 1) or not 0 in img_hough[rho, :]  :
            rhoScale = np.append(rhoScale, rho * rhoRes)
    return [img_hough, rhoScale, thetaScale]
