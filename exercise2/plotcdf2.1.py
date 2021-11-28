import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import rc
  
print("Please enter the filename of the picture:")
file=str(input())

a = [-1, 0]
b = [0, 0]

c = [0, 1]
d = [1/6, 1/6]

e = [1, 4]
f = [3/6, 3/6]

g = [4, 9]
h = [5/6, 5/6]

i = [9, 11]
j = [1, 1]
  
plt.ylabel('$F^X(x)$ = $\mathbb{P}(X) \leq x$') 
plt.xlabel('x')
plt.title('Verteilungsdiagramm fairer Würfel mit Zufallsvariable X')

  
plt.plot(a,b)
plt.plot(c,d)
plt.plot(e,f)
plt.plot(g,h)
plt.plot(i,j)

ax=plt.gca()
ax.set_xlim([-1, 10])
ax.set_ylim([0, 1.1])
plt.yticks([0,1/6,2/6,3/6,4/6,5/6,1],['0','1/6','2/6','3/6','4/6','5/6','1'])


  
plt.savefig('ressources/' + file + 'cdf' + '.png')