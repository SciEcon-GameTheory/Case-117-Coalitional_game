from math import exp
import math
import matplotlib.pyplot as plt
from sympy import *
from scipy.optimize import fsolve
from matplotlib.pyplot import MultipleLocator

class coalition_game():
    def __init__(self, miner_num):
        self.n = miner_num
        self.m = math.ceil(miner_num / 2)
        self.beta = 1/2
        self.lbd = 1

    def generate_d(self,D):
        d=0
        if self.n == 3:
            d = 0.015
        elif self.n == 10 or self.n == 20:
            d = (D*(self.n-3)/(2*(self.n+1)*(1+D*self.beta)))
        return d

    def generate_gama(self, p1, p2, D, lbd2):
        part1 = p1**2 * exp(2*D*lbd2*p1)
        part2 = (p1*p2*( (2*(exp(2*D*lbd2)-1) / (exp(2*D*lbd2*p1)+exp(2*D*lbd2*p2)-2)) - 1))
        part3 = (p1**2 * exp(2*D*lbd2*p1) - p2**2 * exp(2*D*lbd2*p2))
        return ((part1 - part2) / part3)


    def generate_vc(self,D, d):
        ac = self.lbd / (1 + 2*d*self.lbd)
        ass = self.lbd*((self.m + D*self.lbd)/(self.m + self.m*D*self.lbd))
        lbd2 = ac + ass
        p1 = ac/(ac+ass); p2 = 1 - p1
        gama_c = self.generate_gama(p1, p2, D, lbd2)
        return gama_c

    def main(self):
        y_axis = []
        for D in range(1,21):
            d = self.generate_d(D)
            result = self.generate_vc(D, d)
            y_axis.append(result)
        return y_axis

if __name__ == "__main__":
    # plot the Red player: Average rewards
    fig, ax = plt.subplots()
    x_axis = [i for i in range(1,21)]

    rr_y_0 = coalition_game(3).main()
    rr_y_1 = coalition_game(10).main()
    rr_y_2 = coalition_game(20).main()
    rr_y_3 = [0.5 for i in range(1, 21)]

    ax.plot(x_axis, rr_y_0, label='n=3',marker='2')
    ax.plot(x_axis, rr_y_1, label='n=10', marker='+')
    ax.plot(x_axis, rr_y_2, label='n=20', marker='^')
    ax.plot(x_axis, rr_y_3, linestyle='--')

    x_major_locator=MultipleLocator(1)
    y_major_locator=MultipleLocator(0.1)

    ax=plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)

    ax.set_ylim([0.4, 1.1])
    ax.set_xlim([0, 20])

    ax.legend()