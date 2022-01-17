import matplotlib.pyplot as plt
import numpy as np


def verteilungs_funktion(x_param, y_param):
    x_values = range(0, len(x_param))
    y_values = []
    temp = 0
    for item in y_param:
        temp += item
        y_values.append(temp)

    for line in x_values:
        x = np.linspace(line, line + 1)
        y = np.linspace(y_values.__getitem__(line), y_values.__getitem__(line))
        plt.plot(x, y, color='blue')
    plt.scatter(x_values, y_values, color='blue')
    plt.xticks(x_values, x_param)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    plt.ylabel('F(X)')
    plt.xlabel('X')
    x = [3, 4, 5, 5.5, 6, 6.5, 7, 10, 16]
    y = [1 / 11, 1 / 11, 1 / 11, 1 / 11, 1 / 11, 1 / 11, 3 / 11, 1 / 11, 1 / 11]
    verteilungs_funktion(x, y)
