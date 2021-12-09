# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:25:27 2021

@author: Alex
"""

from scipy.stats import expon
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,8)
l = 1/2
y = l * np.exp(-l * x)

a = (-1, 0)
b = (0, 0)

plt.figure()
plt.plot(x, y, color='blue')
plt.plot(a, b, color='blue')
plt.axvline(x=0, ymin=0, color='black')
plt.grid()
plt.xlim(-1, 8)
plt.ylim(0, 0.6)
plt.ylabel(r'$f^X = \frac{1}{2} \cdot e^{-\frac{1}{2} x}$')
plt.xlabel('Zeit $x$ in Stunden um einen Fisch zu fangen')