import numpy as np
from random import choice


print("Please choose the number of drunken sailors!")
bedCount = int(input())
results = []

def writeToFile(filename):
    file = open("ressources/" + filename, "w")
    for t in results:
        file.write(str(t[0]) + "\t" + str(t[1]) + "\n")
    file.close()

def countOccurrences():
    occurrenceSet = set(cache)
    for occurrence in occurrenceSet:
        occurrenceAmount = cache.count(occurrence)
        results.append((occurrence, occurrenceAmount))

def calculateRightChoices():
    beds = []
    tuples = []
    rightChoices = 0
    for i in range(0, bedCount):
        beds.append(i)

    for i in range(0, bedCount):
        bed = choice(beds)
        t = (i, bed)
        tuples.append(t)
        beds.remove(bed)
    
    for t in tuples:
        if t[0] == t[1]:
            rightChoices += 1
    cache.append(rightChoices)
    
print("Please enter the amount of trails:")
trials = int(input())

print("Please enter a data filename:")
file = str(input())

cache = []
for i in range(0, trials):
    calculateRightChoices()

countOccurrences()
writeToFile(file)
    

    