# Day 16
#!/usr/bin/python



def convertToBinary(line):
    binaryString = ""
    for item in line:
        intValue = int(item,base=16)
        value = int(str(bin(intValue))[2:])
        binaryString += f'{value:04}'
    return binaryString

def handleLiteralValuePacket(line):
    packetVersion = line[:3]
    packetType = line[3:6]
    values = []
    for i, char in enumerate(line[6::5]):
        value = i * 5 + 6
        chunk = line[value:value+5]
        values.append(chunk[1:])
        if(chunk[0:1] == "0"):
            break
    sumTotal = int("".join(values),2)
    return sumTotal

def handleOperatorPacket(line):
    packetVersion = line[:3]
    packetType = line[3:6]
    if(line[6:7] == "0"):
        packetLength = int(line[7:22],2)
    elif(line[6:7] == "1"):
        numberOfSubPackets = int(line[7:18],2)

# main part
input = open('demo2.txt','r')
hexadecimalLine = input.readline()

print(hexadecimalLine)

binaryLine = convertToBinary(hexadecimalLine)

print(binaryLine[3:6])

if(binaryLine[3:6] == "100"):
    print(handleLiteralValuePacket(binaryLine))
else:
    print(handleOperatorPacket(binaryLine))