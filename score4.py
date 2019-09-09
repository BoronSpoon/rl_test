import numpy as np

currentBoardBlack = np.zeros((4,4,4), dtype="uint8")
currentBoardWhite = np.zeros((4,4,4), dtype="uint8")
currentBoard = np.zeros((4,4,4), dtype="uint8")

def computeCurrent():
    global currentBoard
    currentBoard = currentBoardBlack + 2*currentBoardWhite

def possibleActions():
    placeArg = np.argwhere(np.count_nonzero(currentBoard, axis=2) != 4)
    #nditer

def valueBMW():
    return currentBoardBlack.sum() - currentBoardWhite.sum()

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
        return True

def judge():
    black = np.any(currentBoardBlack.sum(0)==4) or np.any(currentBoardBlack.sum(1)==4) or np.any(currentBoardBlack.sum(2)==4)
    white = np.any(currentBoardWhite.sum(0)==4) or np.any(currentBoardWhite.sum(1)==4) or np.any(currentBoardWhite.sum(2)==4)
    if black:
        return "black"
    elif white:
        return "white"
    else:
        return "not finished"


def compute(x,y,color):
    computeCurrent()
    possibleActions()
    if place(x,y,color):
        return True, judge(), currentBoardBlack, currentBoardWhite
    else:
        return False, "full", currentBoardBlack, currentBoardWhite
