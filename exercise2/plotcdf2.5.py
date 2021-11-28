import matplotlib.pyplot as plt 
  
print("Please enter the filename of the picture:")
file=str(input())

a = [-2, 0]
b = [0, 0]

c = [0, 1]
d = [1/16, 1/16]

e = [1, 2]
f = [7/16, 7/16]

g = [2, 5]
h = [1, 1]



  
plt.ylabel('$F^X(x)$ = $\mathbb{P}(Y) \leq k$') 
plt.xlabel('k')
plt.title(r'Verteilungsdiagramm zur Zufallsvariable $Y \sim$ Bin(2,$\frac{3}{4}$)')

  
plt.plot(a,b)
plt.plot(c,d)
plt.plot(e,f)
plt.plot(g,h)

ax=plt.gca()
ax.set_xlim([-1, 4])
ax.set_ylim([0, 1.1])
plt.yticks([0,1/16,4/16,7/16,10/16,13/16,1],['0','1/16','4/16','7/16','10/16','13/16','1'])


  
plt.savefig('ressources/' + file + 'cdf' + '.png')