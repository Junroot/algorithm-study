string = input()
bomb = input()

stack = list()
cur = 0
for e in string:
    if len(stack) > 0:
        char, index = stack[-1]
        if index > -1:
            if e == bomb[index+1]:
                stack.append([e, index+1])
            elif e == bomb[0]:
                stack.append([e, 0])
            else:
                stack.append([e, -1])
        else:
            if e == bomb[0]:
                stack.append([e, 0])
            else:
                stack.append([e, -1])
    else:
        if e == bomb[0]:
            stack.append([e, 0])
        else:
            stack.append([e, -1])

    if len(stack) > 0:
        char, index = stack[-1]
        if index == len(bomb)-1:
            for _ in range(len(bomb)):
                stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    for char, index in stack:
        print(char, end='')