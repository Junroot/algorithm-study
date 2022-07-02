import heapq
import sys
inf = sys.maxsize
n, e = map(int, input().split())

graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c
    graph[b][a] = c

v1, v2 = map(int, input().split())

# 1 start
dp = [inf for _ in range(n+1)]
q = []
heapq.heapify(q)
heapq.heappush(q, [0, 1])

while q:
    total, cur = heapq.heappop(q)
    for i in range(1, n+1):
        if graph[cur][i] > 0:
            if total + graph[cur][i] < dp[i]:
                dp[i] = total+graph[cur][i]
                heapq.heappush(q, [dp[i], i])

dp[1] = 0
#print(dp)
# v1 start
dp2 = [inf for _ in range(n+1)]
q = []
heapq.heapify(q)
heapq.heappush(q, [0, v1])

while q:
    total, cur = heapq.heappop(q)
    for i in range(1, n+1):
        if graph[cur][i] > 0:
            if total + graph[cur][i] < dp2[i]:
                dp2[i] = total+graph[cur][i]
                heapq.heappush(q, [dp2[i], i])

dp2[v1] = 0
#print(dp2)

# v2 start
dp3 = [inf for _ in range(n+1)]
q = []
heapq.heapify(q)
heapq.heappush(q, [0, v2])

while q:
    total, cur = heapq.heappop(q)
    for i in range(1, n+1):
        if graph[cur][i] > 0:
            if total + graph[cur][i] < dp3[i]:
                dp3[i] = total+graph[cur][i]
                heapq.heappush(q, [dp3[i], i])

dp3[v2] = 0
print(dp3[v1], dp2[v2])
ans = min(dp[v1] + dp2[v2] + dp3[n], dp[v2] + dp3[v1] + dp2[n])

if ans < inf:
    print(ans)
else:
    print(-1)
