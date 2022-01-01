# author: Levi
import matplotlib.pyplot as plt
import numpy as np


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
    plt.xticks(x_values,x_param)
    plt.grid()
    plt.show()


x = [4, 5, 6, 7]
y = [0.1, 0.3, 0.2, 0.4]
verteilungs_funktion(x, y)
