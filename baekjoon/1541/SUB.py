OriginalInput = input().split('-')
num = []

for i in OriginalInput:
    AddNumber = i.split('+')
    cnt = 0
    for j in AddNumber:
        cnt += int(j)
    num.append(cnt)

FirstNumber = num[0]
for i in range(1, len(num)):
    FirstNumber -= num[i]

print(FirstNumber)
