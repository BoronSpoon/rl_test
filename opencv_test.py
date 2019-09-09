import numpy as np
import cv2

canvas_size = 128
coor = [int(canvas_size*(1/8+1/4*i)) for i in range(4)]
h_margin = int(canvas_size*4/8)
w_margin = int(canvas_size*4/8)
list_srcs = np.float32([[0,0],[0,canvas_size],[canvas_size,canvas_size],[canvas_size,0]])
h_warp = int(canvas_size-h_margin)
w_warp = int(canvas_size+w_margin)
stride = int(canvas_size*2.5/8)
transparency = [1.0,0.7,0.5,0.3]

canvases = [int(255*transparency[::-1][i])*np.ones((canvas_size, canvas_size, 3), dtype="uint8") for i in range(4)]
new_canvas = np.zeros((int(canvas_size+h_margin), int(canvas_size+w_margin), 3), dtype="uint8")
def plot_circle(board, color):
    for i in range(4):
        canvas = canvases[i]
        points = np.nonzero(board[:,:,i])
        if len(points[0]) == 0:
            continue 
        for x,y in zip(points[0], points[1]):
            cv2.circle(canvas,(coor[x], coor[y]), 13, color, -1)

def warp():
    global new_canvas
    list_dsts = np.float32([[0+w_margin, 0],[0,canvas_size-h_margin],[canvas_size,canvas_size-h_margin],[canvas_size+w_margin, 0]])
    perspective_matrix = cv2.getPerspectiveTransform(list_srcs, list_dsts)
    for count, canvas in enumerate(canvases):
        dst = cv2.warpPerspective(canvas, perspective_matrix, (w_warp, h_warp))
        new_canvas[stride*(3-count):stride*(3-count) + h_warp,:,:] += (dst*0.6).astype("uint8")

def plot(currentBoardBlack, currentBoardWhite):
    plot_circle(currentBoardBlack, (255,0,0))
    plot_circle(currentBoardWhite, (0,0,255))
    warp()
    cv2.imshow("test", new_canvas)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        exit()
