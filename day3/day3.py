# Day 3: Binary Diagnostic
#!/usr/bin/python

report = []

input = open('input.txt','r')
for line in input:
    report.append(line.strip())

positions = []
# make pairs for earch bit
for i in range(len(report[0])):
    positions.append([0,0])

lines = []
bitsLength = 0;
# find most common values
for line in report:
    bits = list(line)
    lines.append(bits)
    bitsLength = len(bits)
    for i, bit in enumerate(bits):
        positions[i][int(bit)] += 1

gammaRate = ""
epsilonRate = ""

for position in positions:
    greaterValueIndex = max(zip(position, range(len(position))))[1]
    lesserValueIndex = min(zip(position, range(len(position))))[1]
    gammaRate += str(greaterValueIndex)
    epsilonRate += str(lesserValueIndex)

print("Gamma Rate", gammaRate)
print("Epsilon Rate", epsilonRate)
print("Power: ",int(gammaRate,2) * int(epsilonRate,2))

# part 2
oxygenGeneratorRatingLines = lines.copy()
oxygenGeneratorRating = ""

for i in range(bitsLength):
    zeroCounter = 0
    oneCounter = 0
    # get commonnes rating
    for line in oxygenGeneratorRatingLines:
        if(int(line[i]) == 0):
            zeroCounter += 1
        elif(int(line[i]) == 1):
            oneCounter += 1
    
    value = 0;
    if(oneCounter >= zeroCounter):
        oxygenGeneratorRating += "1"
        value = 1;
    else:
        oxygenGeneratorRating += "0"

    print(value)
    oxygenGeneratorRatingLines = list(filter(lambda x: int(x[i]) == value, oxygenGeneratorRatingLines))
    print(oxygenGeneratorRatingLines)
    if(len(oxygenGeneratorRatingLines) == 1):
        oxygenGeneratorRating = "".join(oxygenGeneratorRatingLines[0])
        break

print("Oxygen Generator Rating: ", oxygenGeneratorRating)

c02ScrubberRatingLines = lines.copy()
c02ScrubberRating = "";

for i in range(bitsLength):
    zeroCounter = 0
    oneCounter = 0
    # get commonnes rating
    for line in c02ScrubberRatingLines:
        if(int(line[i]) == 0):
            zeroCounter += 1
        elif(int(line[i]) == 1):
            oneCounter += 1
    
    value = 0;
    if(oneCounter < zeroCounter):
        c02ScrubberRating += "1"
        value = 1;
    else:
        c02ScrubberRating += "0"

    print(value)
    c02ScrubberRatingLines = list(filter(lambda x: int(x[i]) == value, c02ScrubberRatingLines))
    print(c02ScrubberRatingLines)
    if(len(c02ScrubberRatingLines) == 1):
        c02ScrubberRating = "".join(c02ScrubberRatingLines[0])
        break

print("C02 Scrubber Rating: ", c02ScrubberRating)

print("Life Support Rating: ", int(oxygenGeneratorRating,2) * int(c02ScrubberRating,2))