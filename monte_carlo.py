from score4 import *

v = {}
n = {}
r = 0
stack = [0 for i in range(65)]
current = 0
count = 0
colors = ["black", "white"]

while(1):
    count = 0
    stack = [0 for i in range(65)]
    current = binarize()
    for x,y in possibleActions():
        place(x,y,colors[count%2])
        if actions.shape[0] == 0 or judge()[0]:
            r = valueBMW()
            v[current] += r
            n[current] += 1
            continue
        count += 1
        stack[0] = current
        stack[1] = binarize()
        while(1):
            actions = possibleActions()
            if actions.shape[0] == 0 or judge()[0]:
                r = valueBMW()
                break
            else:
                x,y = actions[np.random.choice(actions.shape[0]]
                place(x,y,colors[count%2])
        for state in stack[:count+1][::-1]:
            v[state] += r
            n[state] += 1
    break

