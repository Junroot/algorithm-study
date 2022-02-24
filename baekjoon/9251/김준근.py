first = input()
second = input()

cache = [[0 for _ in range(len(first))] for _ in range(len(second))]

for i in range(len(second)):
    for j in range(len(first)):
        if first[j] == second[i]:
            if i == 0 or j == 0:
                cache[i][j] = 1
            else:
                cache[i][j] = cache[i - 1][j - 1] + 1
        else:
            next = 0
            if i > 0:
                next = max(next, cache[i - 1][j])
            if j > 0:
                next = max(next, cache[i][j - 1])
            cache[i][j] = next

print(cache[len(second) - 1][len(first) - 1])
