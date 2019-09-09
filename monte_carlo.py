import numpy as np
from score4 import Score4
from cv2Plotter import Plotter
score4 = Score4()
plotter = Plotter()

v = {}
n = {}
r = 0
stack = [0 for i in range(65)]
current = 0
count = 0
colors = ["black", "white"]

def updateVN(state,r):
    if state in v:
        v[state] += r
        n[state] += 1
    else:
        v[state] = r
        n[state] = 1

while(1):
    stack = [0 for i in range(65)]
    current = score4.binarize()
    actions = score4.possibleActions()
    if actions.shape[0] == 0 or score4.judge()[0]:
        r = score4.valueBMW()
        updateVN(current, r)
        break
    score4.saveState()
    for x,y in actions:
        count = 0
        score4.loadState()
        score4.place(x,y,colors[count%2])
        count += 1
        stack[0] = current
        stack[1] = score4.binarize()
        while(1):
            actions = score4.possibleActions()
            if actions.shape[0] == 0 or score4.judge()[0]:
                r = score4.valueBMW()
                break
            else:
                count += 1
                stack[count] = score4.binarize()
                x,y = actions[np.random.choice(actions.shape[0])]
                score4.place(x,y,colors[count%2])
                plotter.plot(score4.currentBoardBlack, score4.currentBoardWhite)
        for state in stack[:count+1][::-1]:
            updateVN(state, r)
    break

