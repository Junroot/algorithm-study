n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
bonus = dict()

for i in range(m):
    a, b = map(int, input().split())
    bonus[a] = b


for i in range(1, n+1):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = max(dp[i-1])
        else:
            dp[i][j] = dp[i-1][j-1] + arr[i]

            if j in bonus:
                dp[i][j]+=bonus[j]

ans = 0
for i in range(n+1):
    ans = max(ans, dp[n][i])

print(ans)