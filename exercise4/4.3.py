# -*- coding: utf-8 -*-

# X:= "Nummer des Seemannes in Bett 1"
# Y:= "Anzahl richtig liegender Seemänner"

# (X, Y)
standardSpace = [(1,0), (1,1), (1,2), (1,3), (1,5),
                 (2,0), (2,1), (2,2), (2,3), (2,5),
                 (3,0), (3,1), (3,2), (3,3), (3,5),
                 (4,0), (4,1), (4,2), (4,3), (4,5),
                 (5,0), (5,1), (5,2), (5,3), (5,5)]



imageSetX = []
imageSetY = []
    
for t in standardSpace:
    if not imageSetX.__contains__(t[0]):
        imageSetX.append(t[0])
    if not imageSetY.__contains__(t[1]):
        imageSetY.append(t[1])
    
print('Imageset of variable X is ' + str(imageSetX))
print('Imageset of variabel Y is ' + str(imageSetY))

# w : p(w)
pY = {0 : 3583/10000, 1 : 3852/10000, 2 : 1669/10000, 3 : 811/10000, 4 : 0, 5 : 85/10000}
pX = {1 : 1/5, 2 : 1/5, 3 : 1/5, 4 : 1/5, 5 : 1/5}



