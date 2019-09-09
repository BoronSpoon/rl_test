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

    def BackPropagate(self,state,r):
        if state in self.v:
            self.v[state] += r
            self.n[state] += 1
        else:
            self.v[state] = r
            self.n[state] = 1

    def expansion(self):
        while(1):
            self.result = {}
            self.stack = [0 for i in range(65)]
            self.current = score4.binarize()
            actions = score4.possibleActions()
            if actions.shape[0] == 0 or score4.judge()[0]:
                self.r = score4.valueBMW()
                self.BackPropagate(self.current, self.r)
                break
            score4.saveState()
            for x,y in actions:
                print("action")
                score4.loadState()
                score4.place(x,y,self.colors[0%2])
                self.result[score4.binarize()] = [x,y]
                self.simulation()
                    for state in self.stack[depth:self.count+1][::-1]:
                        BackPropagate(state, self.r)
        break

    def simulation(self):
        for i in range(100):
            self.count = 0
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

    def UCB1(self,v,n,N):
        return v+self.C*sqrt(log(N)/n)

    def selection(self,depth):
        if depth%2 == 0:
            self.expansion()
            keys = self.result.keys()
            values = [self.UCB1(self.v[k], self.n[k], self.n[self.current]) for k in self.result.keys()]
            nextNode = keys[max(enumerate(values), key=itemgetter(1))]
            x,y = result[nextNode]
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
    if not selection(depth):
        print("end of game")
        cv2.waitKey(10000)
        break
    depth += 1

