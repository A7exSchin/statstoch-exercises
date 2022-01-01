# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 18:21:06 2022

@author: Alex
"""
def searchMap(i):
    for t in map:
        if t[0]==i:
            return t[1]

# A=1,B=2,C=3,D=4
omega = [1,2,3,4]
p = 1/4
K = [10,8,10,16]
map = [(1,10),(2,8),(3,10),(4,16)]
E = 0

# Erwartungswert
for k in K:
    E += k*p

print('Der Erwartungswert ist ' + str(E))

#Varianz
V = 0
for k in K:
    V += (k-E)**2/4

print('Die Varianz ist ' + str(V))

# b)
omega2 = [(1,2),(1,3),(1,4),(2,1),(2,3),(2,4),(3,1),(3,2),(3,4),(4,1),(4,2),(4,3)]
map2 = []

for t in omega2:
    k1 = searchMap(t[0])
    k2 = searchMap(t[1])
    
    mu = 1/2 * (k1 + k2)
    map2.append(t, mu)
    print('Der Erwartungswert für Tupel ' + str(t) + ' ist ' + str(mu))
# c)




