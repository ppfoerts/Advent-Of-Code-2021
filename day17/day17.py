# Day 17
#!/usr/bin/python

def fireProbe(initialVelocity, targetArea):
    init = initialVelocity.copy();
    velocity = initialVelocity;
    position = [0,0]
    highestY = -1000
    while True:
        position[0] += velocity[0]
        position[1] += velocity[1]

        if(velocity[0] >= 1):
            velocity[0] -= 1
        elif(velocity[0] < 0):
            velocity[0] += 1

        velocity[1] -= 1

        if(position[1] > highestY):
            highestY = position[1]

        withinXRange = (position[0] >= targetArea[0][0] and position[0] <= targetArea[0][1])
        withinYRange = (position[1] >= targetArea[1][0] and position[1] <= targetArea[1][1])
        tooFar = (position[0] > targetArea[0][1])
        tooDeep = (position[1] < targetArea[1][0])
        if(withinXRange and withinYRange):
            print("With initial velocity: ",init)
            return highestY
        if(tooDeep or tooFar):
            return -1001


targetArea=[[287,309],[-76,-48]]
#targetArea=[[20,30],[-10,-5]]

initialVelocity = [10,200]
highestY = 0;
numberOfHits = 0

for x in range(0,500):
    for y in range(-1000,1000):
        currentHighestY = fireProbe([x,y],targetArea)
        if(highestY < currentHighestY):
            print(currentHighestY)
            highestY = currentHighestY
        if(currentHighestY != -1001):
            numberOfHits += 1

print("Max Height Reached: ", highestY)
print("Number of Hits: ", numberOfHits)