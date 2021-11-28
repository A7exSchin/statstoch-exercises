import matplotlib.pyplot as plt
import pandas as pd

print("Please enter the filename of the datafile:")
file=str(input())

print("Please enter n:")
n = str(input())

print("Please enter the amount of tries:")
tries = str(input())

print("Please enter the x-Label:")
xLabel = str(input())

print("Please enter the y-Label:")
yLabel = str(input())

print("Please enter the title:")
title = str(input())

data = pd.read_csv("ressources/" + file,sep='\t', lineterminator='\n',header=None)
data = pd.DataFrame(data)

x = data[0]
y = data[1]


plt.figure()

plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title+ ', n='+ n +', '+ tries + ' tries')

plt.bar(x, y)
plt.savefig('ressources/' + file + '.png')