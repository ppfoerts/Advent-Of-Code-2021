#Day12
#!/usr/bin/python

from collections import defaultdict


connections=[]
connectionsDict=defaultdict(list)
paths=[]

with open('input.txt', 'r') as line:
    for item in line:
        connections.append(item.strip().split("-"))
        print(item)

for connection in connections:
    connectionsDict[connection[0]].append(connection[1])
    connectionsDict[connection[1]].append(connection[0])

print(connectionsDict)


def traverse(current,travelledPath):
    if(current == 'end'):
        print(travelledPath)
        return 1
    count = 0
    for nextCave in connectionsDict[current]:
        haveAlreadyGoneThrough = (nextCave in travelledPath)
        if(nextCave.isupper()):
            count += traverse(nextCave,travelledPath)
        elif(nextCave not in travelledPath):
            count += traverse(nextCave,travelledPath | {nextCave})
    return count


numberOfPaths = traverse('start',{'start'})

print("Paths: ",numberOfPaths)