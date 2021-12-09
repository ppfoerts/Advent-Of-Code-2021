#Day6Part2
#!/usr/bin/python

import math


input=[[2,1,9,9,9,4,3,2,1,0],
[3,9,8,7,8,9,4,9,2,1],
[9,8,5,6,7,8,9,8,9,2],
[8,7,6,7,8,9,6,7,8,9],
[9,8,9,9,9,6,5,6,7,8]]

print("Input: ",input)

groups = []

def basin(x,y):
    if(y < 0 or y >= len(input[0]) or x < 0 or x >= len(input) or input[x][y] == 9 or input[x][y] == -1):
        return
    input[x][y] = -1
    print("Value travelled")    
    groups[len(groups)-1] += 1
    basin(x,y-1)
    basin(x,y+1)
    basin(x-1,y)
    basin(x+1,y)
            
        
#find low point
#low point is when top, below, right and left are larger than point
lowPoints = []
basinSizes = []

for x, row in enumerate(input):
    for y, column in enumerate(row):
        groups.append(0)
        basin(x,y)

print(input)
print(groups)

realGroups = []

for value in groups:
    if(value != 0):
        realGroups.append(value)

threeHightestValues = sorted(realGroups, reverse=True)[:3];

finalResult = threeHightestValues[0] * threeHightestValues[1] * threeHightestValues[2]
print("Final Result: ", finalResult)