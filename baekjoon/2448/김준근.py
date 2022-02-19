n = int(input())

result = ["*", "* *", "*****"]
length = 3

while length < n:
    for i in range(length):
        result.append(result[i] + " " * (length * 2 - 1 - (i * 2)) + result[i])

    length *= 2

for i in range(n):
    blank = " " * (n - 1 - i)
    print(blank + result[i] + blank)
