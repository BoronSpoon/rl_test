from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from score4 import compute
import numpy as np

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = {}
y = {}
z = {}
ax.set_xlim(0,4)
ax.set_ylim(0,4)
ax.set_zlim(0,4)

while(1):
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
    z["black"],x["black"],y["black"] = np.nonzero(currentBoardBlack)
    z["white"],x["white"],y["white"] = np.nonzero(currentBoardWhite)
    ax.scatter(z["black"],x["black"],y["black"], c='b', s=300, marker='o') 
    ax.scatter(z["white"],x["white"],y["white"], c='r', s=300, marker='o')
    fig.canvas.draw()