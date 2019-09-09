from score4 import *
from opencv_test import *

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
    count = 0
    stack = [0 for i in range(65)]
    current = binarize()
    actions = possibleActions()
    if actions.shape[0] == 0 or judge()[0]:
        r = valueBMW()
        updateVN(current, r)
        break
    saveState()
    for x,y in actions:
        loadState()
        place(x,y,colors[count%2])
        count += 1
        stack[0] = current
        stack[1] = binarize()
        while(1):
            actions = possibleActions()
            if actions.shape[0] == 0 or judge()[0]:
                r = valueBMW()
                break
            else:
                count += 1
                stack[count] = binarize()
                x,y = actions[np.random.choice(actions.shape[0])]
                place(x,y,colors[count%2])
                plot(currentBoardBlack, currentBoardWhite)
        for state in stack[:count+1][::-1]:
            updateVN(state, r)
    break

