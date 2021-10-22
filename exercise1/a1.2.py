import numpy as np
from random import choice

results = []
occurrences = []

def getBoughtBars():
    cardsLeft = []
    barsBought = 0
    for i in range(1, cardAmount):
        cardsLeft.append(i)
       
    while len(cardsLeft) != 0:
        card = np.random.randint(1, cardAmount)
        if cardsLeft.__contains__(card):
            cardsLeft.remove(card)
        barsBought += 1
        
    occurrences.append(barsBought)
                
def runTrials():
    for i in range(1, trials):
        getBoughtBars()

def countOccurrences():
    occurrenceSet = set(occurrences)
    for occurrence in occurrenceSet:
        occurrenceAmount = occurrences.count(occurrence)
        results.append((occurrence, occurrenceAmount))
        
def calculateMeanValue():
    mean = 0
    for t in results:
        mean += t[0]*(t[1]/trials)
    print("The mean value is " + str(mean))
        
print("Please enter the amount of stickers that are required for a full set:")
cardAmount = int(input())

print("Please enter the amount of collections (trials):")
trials = int(input())

runTrials()
countOccurrences()
print(results)
calculateMeanValue()

