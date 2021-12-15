# Day 15
#!/usr/bin/python

chitons=[]

input = open('input.txt','r')
for i, line in enumerate(input):
    chitons.append(list(map(int,line.strip())))

def prettyPrintChitons(chitons):
    for line in chitons:
        print()
        for item in line:
            print(item,end="")

prettyPrintChitons(chitons)
print()


def traverseFromTop(chitons,y,x, path):
    if(x != 0 or y != 0):
        path.append([y,x])
    if(len(chitons) == x and len(chitons[x]) == y):
        return
    print("Traversing through: ",y,x)
    downPathPossible = (y+1 < len(chitons[x]))
    rightPathPossible = (x+1 < len(chitons))
    if(downPathPossible and rightPathPossible):
        if(chitons[y+1][x] <= chitons[y][x+1]):
            traverseFromTop(chitons,y+1,x,path)
        if(chitons[y+1][x] > chitons[y][x+1]):
            traverseFromTop(chitons,y,x+1,path)

def traverseFromBottom(chitons,y,x,path):

    if(y == 0 and x == 0):
        return path
    print("Traversing through: ",y,x)
    path.append([y,x])
    upPathPossible = (y - 1 >= 0)
    leftPathPossible = (x - 1 >= 0)
    if(upPathPossible and leftPathPossible):
        if(chitons[y-1][x] < chitons[y][x-1]):
            print("Going up")
            traverseFromBottom(chitons,y-1,x,path)
        elif(chitons[y-1][x] >= chitons[y][x-1]):
            print("Going left")
            traverseFromBottom(chitons,y,x-1,path)
        else:
            print("Dead end")
    elif(leftPathPossible and not upPathPossible):
        traverseFromBottom(chitons,y,x-1,path)
    elif(upPathPossible and not leftPathPossible):
        traverseFromBottom(chitons,y-1,x,path)
    else:
        return path

topPath = []
traverseFromTop(chitons,0,0,topPath)

bottomPath = []    
traverseFromBottom(chitons,len(chitons)-1,len(chitons[0])-1,bottomPath)

def findIntersection(topPath,bottomPath):
    print(topPath)
    print(bottomPath)
    latestIntersection = []
    for i, topStep in enumerate(topPath):
        for y, bottomStep in enumerate(bottomPath):
            downStep = [bottomStep[0]+1,bottomStep[1]]
            rightStep = [bottomStep[0],bottomStep[1]+1]
            if(topStep == downStep):
                return [i,y]
            elif(topStep == rightStep):
                return [i,y]

intersection = findIntersection(topPath,bottomPath[::-1])

print(intersection)

def combine(topPath, bottomPath, intersection):
    return topPath[0:intersection[0]+1] + bottomPath[intersection[1]+2:]

combinedPath = combine(topPath,bottomPath[::-1],intersection)

print(combinedPath)
def countPath(chitons, path):
    count = 0
    for step in path:
        count += chitons[step[0]][step[1]]
    return count

print("Path Value: ",countPath(chitons, combinedPath))