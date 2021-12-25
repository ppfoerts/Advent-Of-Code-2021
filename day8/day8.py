# Day 8: Seven Segment Search
#!/usr/bin/python

def checkIfAnagram(string1,string2):
    if(sorted(s1)== sorted(s2)):    
        return True
    else:
        return False

# part 1
input = open('testInput2.txt','r')

for line in input:
    uniquePatterns = []
    outputValues = []
    x, y = line.split("|")
    uniquePatterns = x.split()
    outputValues = y.split()

    mapping = {}
    mapping[1] = [a for a in outputValues if len(a) == 2]
    mapping[4] = [a for a in outputValues if len(a) == 4]
    mapping[7] = [a for a in outputValues if len(a) == 3]
    mapping[8] = [a for a in outputValues if len(a) == 7]

    print(mapping[4])
    mapping[9] = [a for a in outputValues if len(a) == 6 and mapping[4][0] in a]
    mapping[0] = [a for a in outputValues if len(a) == 6 and mapping[7][0] in a]
    mapping[6] = [a for a in outputValues if len(a) == 6]
    print(mapping)

    # get unique instances
# 1 has two values
# 4 has four values
# 7 has three value
# 8 has seven values

"""
decodedValues = []

counter = 0
for outputValue in outputValues:
    sortedOutputValue = sorted(outputValue)
    digits = ""
    if(len(outputValue) == 2):
        digits += '1'
         = sortedOutputValue
        counter += 1
    elif (len(outputValue) == 3): 
        digits += '7'
        mapping[7] = sortedOutputValue
        counter += 1
    elif (len(outputValue) == 4):
        digits += '4'
        mapping[4] = sortedOutputValue
        counter += 1
    elif (len(outputValue) == 7):
        digits += '8'
        mapping[8] = sortedOutputValue
        counter += 1
    elif (len(outputValue) == 6 and mapping[4] in outputValue):
        mapping[9] = sortedOutputValue
    elif (len(outputValue) == 6 and mapping[7] in outputValue):
        mapping[0] = sortedOutputValue
    elif (len(outputValue) == 6):
        mapping[6] = sortedOutputValue

    elif (len(outputValue) == 5 and mapping[1] in outputValue):
        mapping[3] = sortedOutputValue
    elif (len(outputValue) == 5 and mapping[1] in outputValue):
        mapping[2] = sortedOutputValue
    elif (len(outputValue) == 5 and mapping[1] in outputValue):
        mapping[5] = sortedOutputValue

print("Unique Patterns:",uniquePatterns)   
print("Output Values: ",outputValues)


    else:
        print("Value: ", sortedOutputValue)"""

""" for outputValue in outputValues:
    sortedOutputValue = sorted(outputValue)
    mapping = {}
    digits = ""
    if(len(outputValue) == 2):
        digits += '1'
    elif (len(outputValue) == 3): 
        digits += '7'
    elif (len(outputValue) == 4):
        digits += '4'
    elif (len(outputValue) == 7):
        digits += '8'
    elif (sortedOutputValue == sorted("cdfbe")):
        digits += '5'
    elif (sortedOutputValue == sorted("gcdfa")):
        digits += '2'
    elif (sortedOutputValue == sorted("fbcad")):
        digits += '3'
    elif (sortedOutputValue == sorted("cefabd")):
        digits += '9'
    elif (sortedOutputValue == sorted("cdfgeb")):
        digits += '6'
    elif (sortedOutputValue == sorted("cagedb")):
        digits += '0'
    else:
        print("Value: ", sortedOutputValue)
    decodedValues.append(int(digits)) """

print("1,4,7 and 8 appear this many times: ", counter)

print("Decoded Values: ", decodedValues)
