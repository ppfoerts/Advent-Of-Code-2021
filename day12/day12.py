#Day12
#!/usr/bin/python

connections={}
paths=[]

with open('input2.txt', 'r') as line:
    for item in line:
        a, b = item.strip().split("-")
        if a not in connections:
            connections[a] = set({b})
        else:
            connections[a].add(b)
        if b not in connections:
            connections[b] = set({a})
        else:
            connections[b].add(a)


print(connections)


def traverse(current,travelledPath):
    if(current == 'end'):
        #print(travelledPath)
        return 1
    count = 0
    for nextCave in connections[current]:
        haveAlreadyGoneThrough = (nextCave in travelledPath)
        if(nextCave.isupper()):
            count += traverse(nextCave,travelledPath)
        elif(nextCave not in travelledPath):
            count += traverse(nextCave,travelledPath | {nextCave})
    return count


numberOfPaths = traverse('start',{'start'})

print("Paths: ",numberOfPaths)