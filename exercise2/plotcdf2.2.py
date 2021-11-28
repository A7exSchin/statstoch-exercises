import matplotlib.pyplot as plt 
  
print("Please enter the filename of the picture:")
file=str(input())

a = [0, 1]
b = [0, 0]

c = [1, 2]
d = [1/(6 ** 10), 1/(6 ** 10)]

e = [2, 3]
f = [(2/6)**10, (2/6)**10]

g = [3, 4]
h = [(3/6)**10, (3/6)**10]

i = [4, 5]
j = [(4/6)**10, (4/6)**10]

k = [5, 6]
l = [(5/6)**10, (5/6)**10]

m = [6, 8]
n = [(6/6)**10, (6/6)**10]

  
plt.ylabel('$F^X(x)$ = $\mathbb{P}(X) \leq x$') 
plt.xlabel('x')
plt.title('Verteilungsdiagramm Würfelmaximum mit 10 würfen')

  
plt.plot(a,b)
plt.plot(c,d)
plt.plot(e,f)
plt.plot(g,h)
plt.plot(i,j)
plt.plot(k,l)
plt.plot(m,n)

ax=plt.gca()
ax.set_xlim([0, 7])
ax.set_ylim([0, 1.1])
plt.yticks([0,1/6,2/6,3/6,4/6,5/6,1],['0','1/6','2/6','3/6','4/6','5/6','1'])


  
plt.savefig('ressources/' + file + 'cdf' + '.png')