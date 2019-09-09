import numpy as np
import cv2

class Plotter:
    def __init__(self):
        self.canvas_size = 128
        self.coord = [int(self.canvas_size*(1/8+1/4*i)) for i in range(4)]
        self.h_margin = int(self.canvas_size*5/8)
        self.w_margin = int(self.canvas_size*4/8)
        self.list_srcs = np.float32([[0,0],[0,self.canvas_size],[self.canvas_size,self.canvas_size],[self.canvas_size,0]])
        self.h_warp = int(self.canvas_size-self.h_margin)
        self.w_warp = int(self.canvas_size+self.w_margin)
        self.stride = int(self.canvas_size*3/8)
        self.transparency = [1.0,0.7,0.5,0.3]
        self.canvases = [100*np.ones((self.canvas_size, self.canvas_size, 3), dtype="uint8") for i in range(4)]
        self.new_canvas = np.zeros((int(self.canvas_size+self.h_margin), int(self.canvas_size+self.w_margin), 3), dtype="uint8")

    def plot_circle(self, board, color):
        for i in range(4):
            canvas = self.canvases[i]
            points = np.nonzero(board[:,:,i])
            if len(points[0]) == 0:
                continue 
            for x,y in zip(points[0], points[1]):
                cv2.circle(canvas,(self.coord[x], self.coord[y]), 13, color, -1)

    def warp(self):
        list_dsts = np.float32([[0+self.w_margin, 0],[0,self.canvas_size-self.h_margin],[self.canvas_size,self.canvas_size-self.h_margin],[self.canvas_size+self.w_margin, 0]])
        perspective_matrix = cv2.getPerspectiveTransform(self.list_srcs, list_dsts)
        for count, canvas in enumerate(self.canvases):
            dst = cv2.warpPerspective(canvas, perspective_matrix, (self.w_warp, self.h_warp))
            self.new_canvas[self.stride*(3-count):self.stride*(3-count) + self.h_warp,:,:] += (dst*0.7).astype("uint8")

    def plot(self, currentBoardBlack, currentBoardWhite):
        self.canvases = [100*np.ones((self.canvas_size, self.canvas_size, 3), dtype="uint8") for i in range(4)]
        self.new_canvas = np.zeros((int(self.canvas_size+self.h_margin), int(self.canvas_size+self.w_margin), 3), dtype="uint8")
        self.plot_circle(currentBoardBlack, (255,0,0))
        self.plot_circle(currentBoardWhite, (0,0,255))
        self.warp()
        cv2.imshow("test", self.new_canvas)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            exit()
