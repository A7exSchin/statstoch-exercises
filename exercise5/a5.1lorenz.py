# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 17:43:46 2022

@author: Alex
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import StrMethodFormatter

plt.ylabel('kumulierte relative Merkmalssumme')
plt.xlabel('Anteil Merkmalsträger')

u = [3,4,5,5.5,6,6.5,7,7,7,10,16]
n = sum(u)
m = len(u)
i = 0
y = 0

x_values = [0]
y_values = [0]

for j in u:
    i += 1
    x = i/m
    x_values.append(x)
    y += j/n
    y_values.append(y)

plt.xticks(x_values)
plt.gca().xaxis.set_major_formatter(StrMethodFormatter('{x:,.2f}'))
plt.plot(x_values, y_values, '.b-')
plt.grid()
plt.show()