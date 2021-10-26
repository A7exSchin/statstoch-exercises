import matplotlib.pyplot as plt 
  
print("Please enter the filename of the picture:")
file=str(input())
  
a = [0, 1]
b = [3335/10000, 3335/10000]

c = [1, 2]
d = [(3335+4963)/10000, (3335+4963)/10000]

e = [2, 3]
f = [(1702+3335+4963)/10000, (1702+3335+4963)/10000]
  
plt.ylabel('$F^X(x)$ = $\mathbb{P}(X) \leq x$') 
plt.xlabel('x')
plt.title('Verteilungsdiagramm Betrunkene Seeleute')
  
plt.plot(a,b)
plt.plot(c,d)
plt.plot(e,f)
  
plt.savefig('ressources/' + file + 'cdf' + '.png')