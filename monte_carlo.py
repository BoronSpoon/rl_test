import numpy as np
from score4 import Score4
from cv2Plotter import Plotter
from math import *
from operator import itemgetter
score4 = Score4()
plotter = Plotter()

class MonteCarlo:
    def __init__(self):
        self.C = 1 #constant
        self.v = {}
        self.n = {}
        self.r = 0
        self.stack = [0 for i in range(65)]
        self.current = 0
        self.count = 0
        self.colors = ["black", "white"]
        self.result = {}

    def backPropagate(self):
        for state in self.stack[:self.count+1][::-1]:
            self.updateVN(state)

    def updateVN(self, state):
        if state in self.v:
            self.v[state] += self.r
            self.n[state] += 1
        else:
            self.v[state] = self.r
            self.n[state] = 1

    def expansion(self):
        self.result = {}
        self.stack = [0 for i in range(65)]
        self.current = score4.binarize()
        actions = score4.possibleActions()
        if actions.shape[0] == 0 or score4.judge()[0]:
            self.r = score4.valueBMW()
            self.updateVN(self.current)
            return False
        score4.saveState()
        for x,y in actions:
            score4.loadState()
            score4.place(x,y,self.colors[0%2])
            self.result[score4.binarize()] = [x,y]
            self.simulation(x,y)
        return True

    def simulation(self, x,y):
        for i in range(10):
            self.count = 0
            self.stack = [0 for i in range(65)]
            score4.loadState()
            score4.place(x,y,self.colors[self.count%2])
            self.count += 1
            self.stack[0] = self.current
            self.stack[1] = score4.binarize()
            while(1):
                actions = score4.possibleActions()
                if actions.shape[0] == 0 or score4.judge()[0]:
                    self.r = score4.valueBMW()
                    break
                else:
                    self.count += 1
                    self.stack[self.count] = score4.binarize()
                    x,y = actions[np.random.choice(actions.shape[0])]
                    score4.place(x,y,self.colors[self.count%2])
                    #plotter.plot(score4.currentBoardBlack, score4.currentBoardWhite)
            self.backPropagate()

    def UCB1(self,v,n,N):
        return v+self.C*sqrt(log(N)/n)

    def selection(self,depth):
        if depth%2 == 0:
            self.expansion()
            keys = list(self.result.keys())
            if len(keys) == 0:
                return False
            values = [self.UCB1(self.v[k], self.n[k], self.n[self.current]) for k in keys]  
            nextNode = keys[max(enumerate(values), key=itemgetter(1))[0]]
            x,y = self.result[nextNode]
            score4.loadState()
            if not score4.place(x,y,"black"):
                return False
            else:
                return True
        else:
            if not score4.randomChoice("white"):
                return False
            else:
                return True


        
monteCarlo = MonteCarlo()

depth = 0
while(1):
    plotter.plot(score4.currentBoardBlack, score4.currentBoardWhite)
    if not monteCarlo.selection(depth):
        #plotter.plot(score4.currentBoardBlack, score4.currentBoardWhite)
        print("end of game")
        break
    depth += 1

