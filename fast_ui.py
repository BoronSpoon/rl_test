from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from score4 import compute
import numpy as np
from opencv_test import *
import cv2

while(1):
    print("func")
    args = input().split()
    args[0] = int(args[0])
    args[1] = int(args[1])
    args[2] = "black" if args[2] == "b" else "white"
    ret = compute(args[0], args[1], args[2])
    if ret[0]:
        if ret[1] == "black":
            print("black wins")
            break
        elif ret[1] == "white":
            print("white wins")
            break
        else:
            currentBoardBlack, currentBoardWhite = ret[2], ret[3]
    plot(currentBoardBlack, currentBoardWhite)
    