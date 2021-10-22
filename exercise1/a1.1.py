import numpy as np
from random import choice

rightChoices = 0
print("Please choose the number of drunken sailors!")
bedCount = int(input())
beds = []
tuples = []

for i in range(1, bedCount):
    beds.append(i)

for i in range(1, bedCount):
    bed = choice(beds)
    t = (i, bed)
    tuples.append(t)
    beds.remove(bed)
    
for t in tuples:
    print(t)
    if t[0] == t[1]:
        rightChoices += 1
        
print(rightChoices)