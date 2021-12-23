# Day 5: Hydrothermal Venture
#!/usr/bin/python

def prettyPrintLines(lines):
    for line in lines:
        print(line)

def prettyPrintDiagram(diagram):
    for line in diagram:
        print()
        for value in line:
            print(value,end="")
    print()

def markHorizontalLineOnDiagram(diagram,line):
    if(line[0][0] > line[1][0]):
        largerX = line[0][0] + 1
        smallerX = line[1][0]
    else:
        largerX = line[1][0] + 1
        smallerX = line[0][0]

    for x in range(smallerX,largerX):
        diagram[line[0][1]][x] += 1 

def markVerticalLineOnDiagram(diagram,line):
    if(line[0][1] > line[1][1]):
        largerY = line[0][1] + 1
        smallerY = line[1][1]
    else:
        largerY = line[1][1] + 1
        smallerY = line[0][1]

    for y in range(smallerY,largerY):
        diagram[y][line[0][0]] += 1 

def markDiagonalLineOnDiagram(diagram,line):

    if(line[0][1] > line[1][1]):
        largerY = line[0][1] + 1
        smallerY = line[1][1]
        startingX = line[1][0]
        endX = line [0][0]
    else:
        largerY = line[1][1] + 1
        smallerY = line[0][1]
        startingX = line[0][0]
        endX = line [1][0]

    for y in range(smallerY,largerY):
        diagram[y][startingX] += 1 
        if(startingX < endX):
            startingX += 1
        else:
            startingX -= 1
        

def sumOfWhereAtLeastTwoLinesCross(diagram):
    crossSum = 0
    for line in diagram:
        for value in line:
            if (value >= 2):
                crossSum += 1
    print(crossSum)
# part 1

input = open('input.txt','r')

lines = []

for line in input:
    coordinates = line.strip().split("->")
    coordinate = []
    coordinate.append([int(i) for i in coordinates[0].strip().split(",")])
    coordinate.append([int(i) for i in coordinates[1].strip().split(",")])

    lines.append(coordinate)

largestX = 0
largestY = 0

for line in lines:
    for coordinate in line:
        if(coordinate[0] > largestX):
            largestX = coordinate[0]
        if(coordinate[1] > largestY):
            largestY = coordinate[1]

prettyPrintLines(lines)
print("Largest X:",largestX)
print("Largest Y:",largestY)

diagram = [[0 for y in range(largestX+1)] for i in range(largestY+1)]

for line in lines:
    #x1 = x2 or y1 = y2.
    if(line[0][0] == line[1][0]): 
        markVerticalLineOnDiagram(diagram,line)
    elif(line[0][1] == line[1][1]):
        markHorizontalLineOnDiagram(diagram,line)
    else:
        markDiagonalLineOnDiagram(diagram,line)

#prettyPrintDiagram(diagram)
sumOfWhereAtLeastTwoLinesCross(diagram)
