# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
"""
Spyder Editor

This is a temporary script file.
"""
def calcSum(n, k):
    result = 0
    for j in range(1, 7):
        for x in table:
            if (x[0] == n-1 and x[1] == k-j):
                result += x[2]
    return result

n = list(range(1, 41))

table = []

# Triple (n, k, P(W_n = k))
# insert n=1 manually
for i in range(1, 7):
    table.append((1, i, 1/6))

for i in range(2, 41):
    for k in range(1, i * 6 + 1):
        sum = 1/6 * calcSum(i, k)
        table.append((i, k, sum)) 

values = []
for x in table:
    if x[0] == 5:
        values.append((x[1], x[2]))

values = pd.DataFrame(values)
x = values[0]
y = values[1]

print(values)
plt.figure()

plt.xlabel('k')
plt.ylabel('$W_5(k)$')
plt.title('Verteilung von $W_5$')

plt.bar(x, y)
plt.show()

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
    plt.scatter(x_values, y_values, color='blue')
    plt.xticks(x_values,x_param,rotation=90)
    plt.xlabel('k')
    plt.ylabel('$\mathbb{P}(W_5 = k)$')
    plt.title('Diagramm der Verteilugnsfunktion für $\mathbb{P}(W_5 = k)$')
    plt.grid()
    plt.show()

verteilungs_funktion(x, y)