from sys import stdin

n = int(input())
numbers = list(map(int, input().split()))
palindromes = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    palindromes[i][i] = 1

for i in range(n - 1):
    if numbers[i] == numbers[i + 1]:
        palindromes[i][i + 1] = 1

for length in range(3, n + 1):
    for i in range(n - length + 1):
        start = i
        end = i + length - 1
        if numbers[start] == numbers[end] and palindromes[start + 1][end - 1] == 1:
            palindromes[start][end] = 1

m = int(input())

for _ in range(m):
    start, end = map(int, stdin.readline().split())
    print(palindromes[start - 1][end - 1])

