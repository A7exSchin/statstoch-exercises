# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 03:38:29 2022

@author: Alex
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 03:02:44 2022

@author: Alex
"""

import scipy.special as scsp
import matplotlib.pyplot as plt
import numpy as np

n=100
p=1/7
q=6/7
a=0.1

# Suche jetzt k, so dass P_0.5(X <= k) <= 0.1

P = 0
k=0

while (P <= a):
   P += scsp.binom(n, k) * p**k * q**(n-k)
   print('Run: ' + str(k) + ' with probability: ' + str(P))
   k += 1
   
print('10th perc. calc: ' + str(k-2))

# Plot Verteilungsfunktion F^Sn

def verteilungs_funktion(x_param, y_param):
    x_values = range(0, len(x_param))
    y_values = []
    for y in y_param:
        if y == y_param.__getitem__(0):
            y_values.append(y)
        else:
            y_values.append(y + y_values.__getitem__(len(y_values) - 1))

    for line in x_values:
        x = np.linspace(line, line + 1)
        y = np.linspace(y_values.__getitem__(line), y_values.__getitem__(line))
        plt.plot(x, y, color='blue')
    plt.scatter(x_values, y_values, color='blue', label="Verteilungsfunktion $F^{S_n}$")
    plt.xticks(x_values,x_param)
    plt.yticks(np.arange(0, 1.05, 0.1))
    plt.hlines(a, -1, 30, colors='r', linestyles='dashed', label=r"Signifkanzniveau $\alpha$")
    plt.vlines(9, -0.01, 1.1, colors='black', label="Grenze $k^*$")
    plt.legend(loc="upper left")
    plt.ylabel(r'$F^{S_n}(k) = \mathbb{P}(S_n \leq k)$')
    plt.xlabel(r'$k$')
    ax = plt.gca()
    ax.set_xlim([-1, 30])
    ax.set_ylim([0, 1.05])
    plt.grid()
    plt.show()

y = []
P=0
k=0
while (k <= 30):
   P = scsp.binom(n, k) * p**k * q**(n-k)
   y.append(P)
   k += 1

x = range(k)
verteilungs_funktion(x, y)