# Day 1 Sonar sweep
#!/usr/bin/python

input = open('input.txt','r')

depthMeasurements=[]

input = open('input.txt','r')
for i, line in enumerate(input):
    depthMeasurements.append(int(line.strip()))

print(depthMeasurements)

# count everytime it increased
increaseAmount = 0;
lastMeasurement = 0;

for measurement in depthMeasurements:
    if(lastMeasurement != 0):
        if(measurement > lastMeasurement):
            increaseAmount += 1
        lastMeasurement = measurement
    else:
        lastMeasurement = measurement
        continue

print("Increased this many times: ", increaseAmount)

lastWindow = 0
increaseAmountWindow = 0

for i,measurement in enumerate(depthMeasurements):
    if(i == 0 or i == 1):
        continue
    else:
        #print(increaseAmountWindow)
        window = depthMeasurements[i] +  depthMeasurements[i-1] + depthMeasurements[i-2]
        if(lastWindow != 0):
            if(window > lastWindow):
                increaseAmountWindow += 1
        lastWindow = window
    
print("Windows increased this many times: ", increaseAmountWindow)