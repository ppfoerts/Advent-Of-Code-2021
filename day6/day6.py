#Day6
#!/usr/bin/python

input = [[2,1,9,9,9,4,3,2,1,0],
[3,9,8,7,8,9,4,9,2,1],
[9,8,5,6,7,8,9,8,9,2],
[8,7,6,7,8,9,6,7,8,9],
[9,8,9,9,9,6,5,6,7,8]]

#find low point
#low point is when top, below, right and left are larger than point
lowPoints = []

for x, row in enumerate(input):
    for y, column in enumerate(row):

        isLowPoint=bool(True)
        #left
        if(y-1 >= 0):
            if(column > input[x][y-1]):
                isLowPoint=bool(False)
        #right
        if(y+1 < len(input[x])):
            if(column > input[x][y+1]):
                isLowPoint=bool(False)
        #top
        if(x-1 >= 0):
            if(column > input[x-1][y]):
                isLowPoint=bool(False)
        #below
        if(x+1 < len(input)):
            if(column > input[x+1][y]):
                isLowPoint=bool(False)

        if(isLowPoint):
            lowPoints.append(column)
            print("Location: ",x,y)

print("Low Points: ", lowPoints)     

riskValueSum = 0;

for lowPoint in lowPoints:
    riskValueSum += lowPoint + 1

print("Risk value sum",riskValueSum)