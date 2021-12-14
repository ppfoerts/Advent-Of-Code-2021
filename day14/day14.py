#Day14
#!/usr/bin/python

polymer=[]
pairInsertions={}

input = open('input2.txt','r')
for i, line in enumerate(input):
    if(i == 0):
        polymer = list(line.strip())
    elif(i == 1):
        continue
    else:
        a,b = line.strip().split(" -> ")
        pairInsertions[a] = b

print(polymer)
print(pairInsertions)

def insert(polymer,index):
    c = polymer[index] + polymer[index+1]
    value = pairInsertions[c]
    polymer.insert(index+1,value)

def steps(polymer,steps):
    for y in range(steps):
        numberOfPairs = (len(polymer)-1)*2
        for i in range(0,numberOfPairs,2):
            insert(polymer,i)
        print(y)

def prettyPrint(polymer):
    for letter in polymer:
        print(letter,end="")

def getDifferenceBetweenMostAndLeast(polymer):
    #NCHB
    frequencies=[0,0,0,0]
    for letter in polymer:
        if(letter == "N"):
            frequencies[0] += 1
        if(letter == "C"):
            frequencies[1] += 1
        if(letter == "H"):
            frequencies[2] += 1
        if(letter == "B"):
            frequencies[3] += 1

    print(frequencies)
    frequencies.sort()
    return frequencies[-1] - frequencies[0]

steps(polymer,40)
print("Difference: ",getDifferenceBetweenMostAndLeast(polymer))