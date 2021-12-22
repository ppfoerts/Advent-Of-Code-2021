# Day 2 Dive!
#!/usr/bin/python

depth = 0
horizontal = 0

commands=[]

input = open('input.txt','r')
for line in input:
    commands.append(line.strip())

for command in commands:
    splitCommand = command.split()
    if(splitCommand[0] == "forward"):
        horizontal += int(splitCommand[1])
    elif(splitCommand[0] == "down"):
        depth += int(splitCommand[1])
    elif(splitCommand[0] == "up"):
        depth -= int(splitCommand[1])

print("Depth: ",depth)
print("Horizontal Position", horizontal)
print("Multiplied: ", depth * horizontal)

# part 2

depth2 = 0;
horizontal2 = 0;
aim = 0;

for command in commands:
    splitCommand = command.split()
    if(splitCommand[0] == "forward"):
        horizontal2 += int(splitCommand[1])
        depth2 += int(splitCommand[1])*aim
    elif(splitCommand[0] == "down"):
        aim += int(splitCommand[1])
    elif(splitCommand[0] == "up"):
        aim -= int(splitCommand[1])
        
print("Depth: ",depth2)
print("Horizontal Position", horizontal2)
print("Multiplied: ", depth2 * horizontal2)