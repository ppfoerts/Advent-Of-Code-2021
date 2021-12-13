#Day13
#!/usr/bin/python

paper=[["."]]
folds=[]

def countDots(paper):
    count = 0
    for row in paper:
        for item in row:
            if(item == "#"):
                count += 1
    return count

def printPaper(paper):
    for row in paper:
        print()
        for item in row:
            print(item,end="")

def padPaper(paper):
    maxWidth = 0
    for row in paper:
        if(maxWidth < len(row)):
            maxWidth = len(row)
    
    for row in paper:
        diff = maxWidth - len(row)
        for a in range(diff):
            row.append(".")

    print("Max Width: ", maxWidth)

def foldPaper(folds,paper):
    for fold in folds:
        if(fold[0] == "x"):
            foldX(int(fold[1]),paper)
        elif(fold[0] == "y"):
            foldY(int(fold[1]),paper)

def foldY(foldLine,paper):
    fold = 0
    for y in range(foldLine+1,len(paper)):
        fold += 2
        for x in range(len(paper[y])): 
            if(paper[y][x] == "#"):
                paper[y-fold][x] = paper[y][x]

    for y in range(foldLine,len(paper)):
        paper.pop()

def foldX(foldLine,paper):
    for y in range(len(paper)):
        fold = 0
        for x in range(foldLine+1,len(paper[y])):
            fold += 2
            if(paper[y][x] == "#"):
                paper[y][x-fold] = paper[y][x]
    for y in range(len(paper)):
        for x in range(foldLine,len(paper[y])):
            paper[y].pop()

with open('input2.txt', 'r') as line:
    for item in line:
        if(not item.strip()):
            continue
        if(item.startswith('fold')):
            start,end = item.strip().split("=")
            if(start == "fold along x"):
                folds.append(["x",end])
            if(start == "fold along y"):
                folds.append(["y",end])
            continue

        x, y = item.strip().split(",")
        x = int(x)
        y = int(y)

        # add height
        if(y >= len(paper)):
            diff = y - len(paper) + 1
            for a in range(diff):
                paper.append(["."])
        # add length
        if(x >= len(paper[y])):
            diff = x - len(paper[y]) +1
            for a in range(diff):
                paper[y].append(".")

        paper[y][x] = ("#")

padPaper(paper)
foldPaper(folds,paper)
printPaper(paper)
print("Dots: ",countDots(paper))