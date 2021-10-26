import numpy as np

results = []
occurrences = []

def getBoughtBars():
    cardsLeft = []
    barsBought = 0
    for i in range(0, cardAmount):
        cardsLeft.append(i)
       
    while len(cardsLeft) != 0:
        card = np.random.randint(0, cardAmount)
        if cardsLeft.__contains__(card):
            cardsLeft.remove(card)
        barsBought += 1
        
    occurrences.append(barsBought)
                
def runTrials():
    for i in range(0, trials):
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
    
def calculateAmountToGetNew():
    
    for i in range(0, cardAmount):
        cardsLeftToCollect = []
        result = 0
        
        # Add all cards to an array
        for j in range(0, cardAmount):
            cardsLeftToCollect.append(j)
        
        # Remove i cards to simulate a partial collection
        for k in range(0, i):
            cardsLeftToCollect.remove(k)
        
        # Debugging prints
        print("Loop is " + str(i))
        print("Cards left is " + str(cardsLeftToCollect))
        
        # Calculate the amount of bars that need to be bought for getting one
        # new card
        for l in range(1, trials):
            cardFound=False
            barsBought = 0
            while (not cardFound):
                card = np.random.randint(1, cardAmount)
                if cardsLeftToCollect.__contains__(card):
                    cardFound=True
                barsBought += 1
            result += barsBought/trials
        
        print("Mean amount to get new: " + str(result))
        
def writeToFile(filename):
    file = open("ressources/" + filename, "w")
    for t in results:
        file.write(str(t[0]) + "\t" + str(t[1]) + "\n")
    file.close()
    
print("Please enter the amount of stickers that are required for a full set:")
cardAmount = int(input())

print("Please enter the amount of collections (trials):")
trials = int(input())

print("Please enter a filename for the datafile:")
file = str(input())

runTrials()
countOccurrences()
print(results)
writeToFile(file)
calculateMeanValue()
calculateAmountToGetNew()

