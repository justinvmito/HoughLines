import math
from bisect import bisect_left

def findClosest(angle):
    angleList = [0, math.pi / 4, math.pi / 2, math.pi * 3/4]
    i = bisect_left(angleList, angle)
    if i == 0:
        return angleList[0]
    if i == len(angleList):
        return angleList[-1]
    left = angleList[i - 1]
    right = angleList[i]
    if right - angle > angle - left:
        return left
    else:
        return right