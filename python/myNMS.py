import numpy as np
import math
from findClosest import findClosest
def myNMSDirectional(angles, img):
    # YOUR CODE HERE
    windowSize = 3
    output = np.zeros((img.shape[0], img.shape[1]))
    # determine kernel width and necessary padding sizes
    padding = int(windowSize/2)
    # paddedI refers to the padded img
    paddedI = np.pad(img,((padding,padding), (padding,padding)), 'edge')
    for y in np.arange(angles.shape[0]):
        # the variables tempy and tempx are used to convert the coordinates from unpadded to padded. Refers to the padded coords.
        tempy = y + padding
        for x in np.arange(angles.shape[1]):
            tempx = x + padding

            # Map the gradient angle to the closest angle
            angle = None
            if angles[y, x] < 0 :
                angle = math.pi + angles[y, x]
            else :
                angle = angles[y,x]
            theta = findClosest(angle)
            # Uses ELIFs rather than match case since I couldnt get it to work with expressions like (math.pi / 4)
            # Performs the comparison with the neighbors along the gradient. Each if/elif is for a different angle.
            if theta == (math.pi / 2):
                if (paddedI[tempy, tempx - 1] > paddedI[tempy, tempx]) or (paddedI[tempy, tempx + 1] > paddedI[tempy, tempx]):
                    output[y, x] = 0
                else :
                    output[y, x] = img[y, x]
            elif theta == (math.pi / 4):
                if (paddedI[tempy + 1, tempx + 1] > paddedI[tempy, tempx]) or (paddedI[tempy - 1, tempx - 1] > paddedI[tempy, tempx]):
                    output[y, x] = 0
                else :
                    output[y, x] = img[y, x]
            elif theta == 0:
                if (paddedI[tempy - 1, tempx] > paddedI[tempy, tempx]) or (paddedI[tempy + 1, tempx] > paddedI[tempy, tempx]):
                    output[y, x] = 0
                else :
                    output[y, x] = img[y, x]
            elif theta == (math.pi * 3/4):
                if (paddedI[tempy + 1, tempx - 1] > paddedI[tempy, tempx]) or (paddedI[tempy - 1, tempx + 1] > paddedI[tempy, tempx]):
                    output[y, x] = 0
                else :
                    output[y, x] = img[y, x]
    return output    

def myNMS(nLines, img):
    windowSize = 3
    padding = int(windowSize/2)
    padding = int(windowSize/2)
    # paddedI refers to the padded img
    paddedI = np.pad(img,((padding,padding), (padding,padding)), 'constant', constant_values = 0)
    count = 0
    rhos = np.array([])
    thetas = np.array([])
    while count < nLines :
        current = np.argmax(img)
        y, x = np.unravel_index(current, img.shape) #rho, theta
        tempy = y + padding
        tempx = x + padding
        neighborhood = paddedI[(tempy - padding):(tempy + padding + 1), (tempx - padding) : (tempx + padding + 1)]
        if np.max(neighborhood) <= img[y, x] and not (np.argmin(neighborhood) == -1):
            rhos = np.append(rhos, y)
            thetas = np.append(thetas, x)
            count += 1
        # setting it to -1 means the index previously held a high(er) value
        # being -1, a value out of the normal range, allows it to not interfere with argmax, while being
        # easily detectible by argmin
        img[y, x] = -1
    return(rhos, thetas)