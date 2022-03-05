import sys
n = int(sys.stdin.readline())

weights = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

questions = list(map(int, sys.stdin.readline().split()))

weights_sum = 0

for i in range(n):
    weights_sum += weights[i]

weight_table = [0 for _ in range(weights_sum + 2)]
check = [[0 for _ in range(weights_sum + 2)] for _ in range(n + 1)]

ans = []

def dp(cur, left, right):
    diff = abs(left - right)
    if diff not in ans:
        ans.append(diff)
    if cur == n:
        return

    weight_table[diff] = 1
    weight = weights[cur]

    if check[cur][diff] == 0:
        dp(cur + 1, left + weight, right)
        dp(cur + 1, left, right + weight)
        dp(cur + 1, left, right)
        check[cur][diff] = 1


dp(0, 0, 0)


for i in range(m):
    if questions[i] in ans:
        print('Y', end='')
    else:
        print('N', end='')
    if i < m - 1:
        print(' ',end='')
