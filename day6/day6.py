# Day 6: Lanternfish
#!/usr/bin/python

input = open('input.txt','r')

lanternFishes = [int(x) for x in input.readline().split(",")]

print(lanternFishes)

days = 256

for day in range(days):
    # decrease time
    lanternFishes = [x-1 for x in lanternFishes]
    for f, fish in enumerate(lanternFishes):
        if(fish == -1):
            lanternFishes[f] = 6
            lanternFishes.append(8)
    print("Day: ",day)

print("Number of fishes: ", len(lanternFishes))

