# Imports
import matplotlib.pyplot as plt
import random as rand
import numpy as np


# portaCom() function
def portaCom(n, c):
    c1 = c2 = x = 0
    c1_list = []
    c2_list = []
    x_list = []
    profit_list = []
    mean, sd = 15000, 4500
    profit = sum_profit = max_profit = max_loss = profit_times = 0
    counter = 0
    
    while counter < n:
        r1 = rand.random()
        r2 = rand.random()

        if r1 < 0.1:
            c1 = 43
        elif r1 < 0.3:
            c1 = 44
        elif r1 < 0.7:
            c1 = 45
        elif r1 < 0.9:
            c1 = 46
        elif r1 <= 1:
            c1 = 47

        c2 = 80 + 20 * r2

        x = np.random.normal(mean, sd)

        profit = (249-c1-c2)*x - 1000000

        # store values in lists
        c1_list.append(c1)
        c2_list.append(c2)
        x_list.append(x)
        profit_list.append(profit)


        if profit > 0:
            sum_profit += profit
            profit_times += 1
        
        if max_profit < profit:
            max_profit = profit
        
        if max_loss > profit:
            max_loss = profit

        counter += 1
        
    print 'Probability of loss = ', 1 - (profit_times*1.0 / n)
    print 'Maximum profit = ', max_profit
    print 'Maximum loss = ', max_loss
    print 'Average profit = ', sum_profit/profit_times

    plt.hist(c1_list, bins=[43, 44, 45, 46, 47, 48], rwidth=0.95, color=c)
    plt.xlabel('c1')
    plt.ylabel('Frequency')
    plt.show()

    plt.hist(c2_list, bins=10, rwidth=0.95, color=c)
    plt.xlabel('c2')
    plt.ylabel('Frequency')
    plt.show()

    plt.hist(x_list, bins=10, rwidth=0.95, color=c)
    plt.xlabel('x')
    plt.ylabel('Frequency')
    plt.show()

    plt.hist(profit_list, bins=10, rwidth=0.95, color=c)
    plt.xlabel('profit')
    plt.ylabel('Frequency')
    plt.show()


# 10 runs simulation
portaCom(10, "orange")


# 1000,000 runs simulation
portaCom(1000000, "b")



