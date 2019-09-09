import numpy as np
from gmpy2 import mpz

currentBoardBlack = np.zeros((4,4,4), dtype="uint8")
currentBoardWhite = np.zeros((4,4,4), dtype="uint8")
currentBoard = np.zeros((4,4,4), dtype="uint8")

def computeCurrent():
    global currentBoard
    currentBoard = currentBoardBlack + 2*currentBoardWhite

def possibleActions():
    return np.argwhere(np.count_nonzero(currentBoard, axis=2) != 4)

def valueBMW():
    return currentBoardBlack.sum() - currentBoardWhite.sum()

def binarize():
    return int(''.join([mpz(num).digits() for num in currentBoard.flatten()]), 3)

def place(x,y,color):
    global currentBoardBlack, currentBoardWhite
    if color == "black":
        currentBoardColor = currentBoardBlack
    else:
        currentBoardColor = currentBoardWhite
    nonzero = np.count_nonzero(currentBoard[x,y,:])
    if nonzero == 4:
        return False
    else:
        currentBoardColor[x,y,nonzero] = 1
        computeCurrent()
        return True

def judge():
    black = np.any(currentBoardBlack.sum(0)==4) or np.any(currentBoardBlack.sum(1)==4) or np.any(currentBoardBlack.sum(2)==4)
    white = np.any(currentBoardWhite.sum(0)==4) or np.any(currentBoardWhite.sum(1)==4) or np.any(currentBoardWhite.sum(2)==4)
    if black:
        return True, "black"
    elif white:
        return True, "white"
    else:
        return False, "not finished"


def compute(x,y,color):
    computeCurrent()
    if place(x,y,color):
        return True, judge()[0], currentBoardBlack, currentBoardWhite
    else:
        return False, "full", currentBoardBlack, currentBoardWhite
