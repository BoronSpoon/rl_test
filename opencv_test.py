import numpy as np
import cv2

a = np.zeros((4,4,4), dtype="uint8")
a[0,1,1] =a[0,3,1] =a[1,1,1] =a[1,1,0] = 1
canvas_size = 128
coor = [int(canvas_size*(1/8+1/4*i)) for i in range(4)]
h_margin = canvas_size*5/8
w_margin = canvas_size*4/8
list_srcs = np.float32([[0,0],[0,canvas_size],[canvas_size,canvas_size],[canvas_size,0]])
h_warp = int(canvas_size-h_margin)
w_warp = int(canvas_size+w_margin)
stride = int(canvas_size*3/8)

canvases = [np.zeros((canvas_size, canvas_size, 3), dtype="uint8") for i in range(4)]
new_canvas = np.zeros((int(canvas_size*5/8), int(canvas_size*5/8), 3), dtype="uint8")
def plot_circle():
    global canvases
    for i in range(4):
        canvas = canvases[i]
        points = np.nonzero(a[:,:,i])
        if len(points[0]) == 0:
            continue 
        for x,y in zip(points[0], points[1]):
            cv2.circle(canvas,(coor[x], coor[y]), 13, (255,0,0), -1)

def warp():
    global new_canvas
    list_dsts = np.float32([[0+h_margin, 0+w_margin],list_srcs[1],list_srcs[2],[canvas_size+h_margin, 0+w_margin]])
    perspective_matrix = cv2.getPerspectiveTransform(list_srcs, list_dsts)
    for count, canvas in enumerate(canvases):
        dst = cv2.warpPerspective(canvas, perspective_matrix, (h_warp, w_warp))
        new_canvas[stride*count:stride*count + h_warp,:,:] += dst*0.5

plot_circle()
warp()
cv2.imshow("test", new_canvas)
cv2.waitKey(1000)
