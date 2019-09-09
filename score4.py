import numpy as np
from gmpy2 import mpz
from copy import deepcopy

class Score4:
    def __init__(self):
        self.currentBoardBlack = np.zeros((4,4,4), dtype="uint8")
        self.currentBoardWhite = np.zeros((4,4,4), dtype="uint8")
        self.currentBoard = np.zeros((4,4,4), dtype="uint8")
        self.savedBoard = [None, None]
        self.mask1 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        self.mask2 = np.array([[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]])
        self.mask3 = np.array([
            [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
            [[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]],
            [[0,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]],
            [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
        ])
        self.mask4 = np.array([
            [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]],
            [[0,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]],
            [[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]],
            [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        ])
        self.mask5 = np.array([
            [[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,0,0,0]],
            [[0,0,0,0],[0,0,0,0],[0,1,0,0],[0,0,0,0]],
            [[0,0,0,0],[0,0,1,0],[0,0,0,0],[0,0,0,0]],
            [[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        ])
        self.mask6 = np.array([
            [[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
            [[0,0,0,0],[0,0,1,0],[0,0,0,0],[0,0,0,0]],
            [[0,0,0,0],[0,0,0,0],[0,1,0,0],[0,0,0,0]],
            [[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
        ])

    def computeCurrent(self):
        self.currentBoard = self.currentBoardBlack + 2*self.currentBoardWhite

    def saveState(self):
        self.savedBoard = [deepcopy(self.currentBoardBlack), deepcopy(self.currentBoardWhite)]

    def loadState(self):
        self.currentBoardBlack, self.currentBoardWhite = deepcopy(self.savedBoard)
        self.computeCurrent()

    def possibleActions(self):
        return np.argwhere(np.count_nonzero(self.currentBoard, axis=2) != 4)

    def valueBMW(self):
        return self.currentBoardBlack.sum() - self.currentBoardWhite.sum()
    
    def valueWinLose(self):
        ret = self.judge()[1]
        if ret == "Black Wins":
            return 1
        elif ret == "White Wins":
            return -1
        elif ret == "Full":
            return 0
        else:
            print("error")

    def binarize(self):
        return int(''.join([mpz(num).digits() for num in self.currentBoard.flatten()]), 3)

    def place(self,x,y,color):
        if color == "black":
            currentBoardColor = self.currentBoardBlack
        elif color == "white":
            currentBoardColor = self.currentBoardWhite
        else:
            print(error)
        nonzero = np.count_nonzero(self.currentBoard[x,y,:])
        if nonzero == 4:
            return False
        else:
            currentBoardColor[x,y,nonzero] = 1
            self.computeCurrent()
            return True

    def randomChoice(self, color):
        actions = self.possibleActions()
        if actions.shape[0] == 0:
            return False
        x,y = actions[np.random.choice(actions.shape[0])]
        return self.place(x,y,color)
        

    def judge(self):
        black = \
        np.any(self.currentBoardBlack.sum(0)==4) or \
        np.any(self.currentBoardBlack.sum(1)==4) or \
        np.any(self.currentBoardBlack.sum(2)==4) or \
        np.any(np.apply_over_axes(np.sum,self.currentBoardBlack*self.mask1,[0,1])[0,0,:]==4) or \
        np.any(np.apply_over_axes(np.sum,self.currentBoardBlack*self.mask1,[1,2])[:,0,0]==4) or \
        np.any(np.apply_over_axes(np.sum,self.currentBoardBlack*self.mask1,[2,0])[0,:,0]==4) or \
        np.any(np.apply_over_axes(np.sum,self.currentBoardBlack*self.mask2,[0,1])[0,0,:]==4) or \
        np.any(np.apply_over_axes(np.sum,self.currentBoardBlack*self.mask2,[1,2])[:,0,0]==4) or \
        np.any(np.apply_over_axes(np.sum,self.currentBoardBlack*self.mask2,[2,0])[0,:,0]==4) or \
        np.sum(self.currentBoardBlack*self.mask3)==4 or \
        np.sum(self.currentBoardBlack*self.mask4)==4 or \
        np.sum(self.currentBoardBlack*self.mask5)==4 or \
        np.sum(self.currentBoardBlack*self.mask6)==4

        white = \
        np.any(self.currentBoardWhite.sum(0)==4) or \
        np.any(self.currentBoardWhite.sum(1)==4) or \
        np.any(self.currentBoardWhite.sum(2)==4) or \
        np.any(np.apply_over_axes(np.sum,self.currentBoardWhite*self.mask1,[0,1])[0,0,:]==4) or \
        np.any(np.apply_over_axes(np.sum,self.currentBoardWhite*self.mask1,[1,2])[:,0,0]==4) or \
        np.any(np.apply_over_axes(np.sum,self.currentBoardWhite*self.mask1,[2,0])[0,:,0]==4) or \
        np.any(np.apply_over_axes(np.sum,self.currentBoardWhite*self.mask2,[0,1])[0,0,:]==4) or \
        np.any(np.apply_over_axes(np.sum,self.currentBoardWhite*self.mask2,[1,2])[:,0,0]==4) or \
        np.any(np.apply_over_axes(np.sum,self.currentBoardWhite*self.mask2,[2,0])[0,:,0]==4) or \
        np.sum(self.currentBoardWhite*self.mask3)==4 or \
        np.sum(self.currentBoardWhite*self.mask4)==4 or \
        np.sum(self.currentBoardWhite*self.mask5)==4 or \
        np.sum(self.currentBoardWhite*self.mask6)==4

        full = np.all(self.currentBoard != 0)
        if black:
            return True, "Black Wins"
        elif white:
            return True, "White Wins"
        elif full:
            return True, "Full"
        else:
            return False, "not finished"


    def compute(self,x,y,color):
        self.computeCurrent()
        if place(x,y,color):
            return True, self.judge()[0], self.currentBoardBlack, self.currentBoardWhite
        else:
            return False, "full", self.currentBoardBlack, self.currentBoardWhite
