import numpy as np
import cv2

a = np.zeros((4,4,4), dtype="uint8")
a[0,1,1] =a[0,3,1] =a[1,1,1] =a[1,1,0] = 1
canvas_size = 128
x_coor = [int(canvas_size*(1/8+1/4*i)) for i in range(4)]
y_coor = x_coor

canvases = [np.zeros((canvas_size, canvas_size, 3), dtype="uint8") for i in range(4)]
def plot_circle():
    global canvases
    for i in range(4):
        canvas = canvases[i]
        points = np.nonzero(a[:,:,i])
        if len(points[0]) == 0:
            continue 
        for x,y in zip(points[0], points[1]):
            cv2.circle(canvas,(x_coor[x], y_coor[y]), 13, (255,0,0), -1)

plot_circle()
for count, canvas in enumerate(canvases):
    cv2.imshow(f"test {count}", canvas)
    cv2.waitKey(1000)
