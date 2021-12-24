# Day 7: The Treachery of Whales
#!/usr/bin/python

from statistics import median


def mean(dataset):
    return sum(dataset) / len(dataset)

def getSequenceValue(value):
    newValue = 0
    for i in range(1,value+1):
        newValue += i
    return newValue

def getFuelCosts(crabPositions,position):
    fuelCost = 0
    for crab in crabPositions:
        fuelCost += getSequenceValue(int(abs(crab - position)))
    return fuelCost

# part 1
input = open('input.txt','r')

crabPositions = [int(x) for x in input.readline().split(",")]

print("Crab positions: ", crabPositions)
fuelCosts = {}

for i in range(500):
    fuelCosts[i] = getFuelCosts(crabPositions,i)

print("Fuel Costs: ",fuelCosts)

temp = min(fuelCosts.values())
res = [key for key in fuelCosts if fuelCosts[key] == temp]
  
# printing result 
print("Key with minimum values is : " + str(res))
print("with fuel cost of: ",fuelCosts[res])
