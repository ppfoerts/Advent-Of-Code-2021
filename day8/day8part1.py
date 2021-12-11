#Day7
#!/usr/bin/python

input = [
[5,4,8,3,1,4,3,2,2,3],
[2,7,4,5,8,5,4,7,1,1],
[5,2,6,4,5,5,6,1,7,3],
[6,1,4,1,3,3,6,1,4,6],
[6,3,5,7,3,8,5,4,7,8],
[4,1,6,7,5,2,4,6,4,5],
[2,1,7,6,8,4,1,7,2,1],
[6,8,8,2,8,8,1,1,3,4],
[4,8,4,6,8,4,8,5,5,4],
[5,2,8,3,7,5,1,5,2,6]]

input = [
[8,5,4,8,3,3,5,6,4,4],
[6,5,7,6,5,2,1,7,8,2],
[1,2,2,3,6,7,7,7,6,2],
[1,2,8,4,7,1,3,1,1,3],
[6,1,2,5,6,5,4,7,7,8],
[6,4,3,5,7,2,6,8,4,2],
[5,6,6,4,1,7,5,5,5,6],
[1,4,4,5,7,3,6,5,5,6],
[2,2,4,8,4,7,3,5,6,8],
[6,4,5,1,4,7,3,5,2,6]
]

# function to increase power level by 1
def increasePowerLevel(input):
    for x in range(len(input)):
        for y in range(len(input)):
            input[x][y] += 1
    return input

def flash(input,x,y):
    if(input[x][y] > 9):
        #increase all values around by 1
        #first check if there are adjacent
        topExists = (x + 1 < len(input))
        bottomExists = (x - 1 >= 0)
        rightExists = (y + 1 < len(input[x]))
        leftExists = (y - 1 >= 0)
        input[x][y] = -1
        if(topExists and input[x+1][y] != -1):
            input[x+1][y] += 1
            flash(input,x+1,y)
        if(bottomExists and input[x-1][y] != -1):
            input[x-1][y] += 1
            flash(input,x-1,y)
        if(rightExists and input[x][y+1] != -1):
            input[x][y+1] += 1
            flash(input,x,y+1)
        if(leftExists and input[x][y-1] != -1):
            input[x][y-1] += 1
            flash(input,x,y-1)
        if(topExists and rightExists and input[x+1][y+1] != -1):
            input[x+1][y+1] += 1
            flash(input,x+1,y+1)
        if(topExists and leftExists and input[x+1][y-1] != -1):
            input[x+1][y-1] += 1
            flash(input,x+1,y-1) 
        if(bottomExists and rightExists and input[x-1][y+1] != -1):
            input[x-1][y+1] += 1
            flash(input,x-1,y+1)
        if(bottomExists and leftExists and input[x-1][y-1] != -1):
            input[x-1][y-1] += 1
            flash(input,x-1,y-1)
    else:
        return

# function to do flash
def flashBegin(input):
    for x in range(len(input)):
        for y in range(len(input[x])):
            flash(input,x,y)
                
    return input

def resetPower(input,step):
    numberOfFlashes = 0;
    for x in range(len(input)):
        for y in range(len(input)):
            if(input[x][y] == -1):
                numberOfFlashes += 1
                input[x][y] = 0
    if(numberOfFlashes == len(input) * len(input[x])):
        print("Synchronized Flash on Step:", step)
    return numberOfFlashes  


def printMatrix(input):
    for x in range(len(input)):
        print()
        for y in range(len(input)):
            print(input[x][y],end="")

totalNumberOfFlashes = 0; 
print("Total Elements: ", len(input) * len(input[0]))  
#make loop for steps
for step in range(500):
    print(step)
    increasePowerLevel(input)
    flashBegin(input)
    totalNumberOfFlashes += resetPower(input,step)

printMatrix(input)
print()
print("Number of Flashes: ", totalNumberOfFlashes)