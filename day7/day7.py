#Day6
#!/usr/bin/python

import re

illegalPoints = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

input = ['[({(<(())[]>[[{[]{<()<>>',
'[(()[<>])]({[<{<<[]>>(',
'{([(<{}[<>[]}>{[]{[(<()>',
'(((({<>}<{<{<>}{[]{[]{}',
'[[<[([]))<([[{}[[()]]]',
'[{[{({}]{}}([{[{{{}}([]',
'{<[[]]>}<{[{[{[]{()[[[]',
'[<(<(<(<{}))><([]([]()',
'<{([([[(<>()){}]>(<<{{',
'<{([{{}}[<[[[<>{}]]]>[]]']

#goal is to find unclosed brackets, so only if a right bracket does not have a left
illegalBrackets=[]
for x,row in enumerate(input):
    print("Row: ",x)
    print("contents: ",row)
    stack=[]
    for y,column in enumerate(row):
        if(column == ')'):
            if(stack[-1] == '('):
               stack.pop()
            else:
                print("Illegal Character found: ) ")
                illegalBrackets.append(column)
                break
        elif(column == ']'):
            if(stack[-1] == '['):
               stack.pop()
            else:
                print("Illegal Character found: ] ")
                illegalBrackets.append(column)
                break
        elif(column == '}'):
            if(stack[-1] == '{'):
               stack.pop()
            else:
                print("Illegal Character found: } ")
                illegalBrackets.append(column)
                break
        elif(column == '>'):
            if(stack[-1] == '<'):
               stack.pop()
            else:
                print("Illegal Character found: > ")
                illegalBrackets.append(column)
                break 
        else:
            stack.append(column)

print("Illegal Brackets",illegalBrackets)
print(f'Total illegal points: {sum([illegalPoints[brackets] for brackets in illegalBrackets])}')