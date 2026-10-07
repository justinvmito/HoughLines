import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

def myImageFilter(img0, h):
    # YOUR CODE HERE
    img1 = np.zeros((img0.shape[0], img0.shape[1]))
    # invert h for convolution
    kernel = np.flip(h)

    # determine kernel width and necessary padding sizes
    paddingVert = int(h.shape[0]/2)
    paddingHori = int(h.shape[1]/2)
    padded = np.pad(img0, ((paddingVert,paddingVert), (paddingHori,paddingHori)), 'edge')

    for y in np.arange(img1.shape[0]):
        # the variables tempy and tempx are used to convert the coordinates from unpadded to padded.
        tempy = y + paddingVert
        for x in np.arange(img1.shape[1]):
            tempx = x + paddingHori

            img1[y, x] = np.average(np.multiply(padded[tempy-paddingVert:tempy+paddingVert+1,tempx-paddingHori:tempx+paddingHori+1], h))

    return img1


# Testing with a box kernel
'''
datadir    = 'data'      # the directory containing the images
resultsdir = 'results'   # the directory for dumping results

kernel = np.array([[1,1,1], [1,1,1], [1,1,1]])
convolved = None
for file in os.listdir(datadir):
    if file.endswith('img01.jpg'):
        file = os.path.splitext(file)[0]
        
        # read in images
        img = cv2.imread('%s/%s.jpg' % (datadir, file))

        if (img.ndim == 3):
            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        img = np.float32(img) / 255
        convolved = myImageFilter(img,kernel)
        plt.imshow(img)
        plt.show()
plt.imshow(convolved)
plt.show()
'''
