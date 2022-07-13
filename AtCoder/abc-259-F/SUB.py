import math

n = int(input())
max_choice = list(map(int, input().split()))
max_choice.insert(0, 0)

arr = [[] for _ in range(n+1)]
dp = [[0 for _ in range(2)] for _ in range(300001)]

for i in range(n-1):
    start, end, w = map(int, input().split())
    arr[start].append([end, w])
    arr[end]. append([start, w])


def dfs(cur, parent):
    childs = list()
    for e in arr[cur]:
        child = e[0]
        weight = e[1]
        if child == parent:
            continue
        dfs(child, cur)
        childs.append(dp[child][0] + weight - dp[child][1])
        dp[cur][0] += dp[child][1]
        dp[cur][1] += dp[child][1]
    childs.sort(reverse=True)

    for i in range(len(childs)):
        if childs[i] <= 0:
            break
        if i < max_choice[cur] - 1:
            dp[cur][0] += childs[i]
        if i < max_choice[cur]:
            dp[cur][1] += childs[i]

    if max_choice[cur] == 0:
        dp[cur][0] = -math.inf


dfs(1, -1)
print(dp[1][1])

