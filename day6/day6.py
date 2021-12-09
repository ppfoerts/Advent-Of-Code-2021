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
        print("Location: ",x,y)
        print("Value: ",column)
        isLowPointer=bool(True)
        #left
        if(y-1 > 0):
            print("has left side")
        #right
        if(y+1 < len(input[x])):
            print("has right side")
        #top
        if(x-1 > 0):
            print("has top side")
        #below
        if(x+1 < len(input)):
            print("has bottom")
        #left
        #right