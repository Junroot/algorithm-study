import heapq
import sys

n = int(input())
m = int(input())

arr = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    arr[start].append([end, cost])

start, end = map(int, input().split())

dist = [n*100000+1 for _ in range(n+1)]
path = [[] for _ in range(n+1)]
path[start].append(start)
q = []
heapq.heapify(q)
q.append([0, start])

dist[start] = 0
while q:
    total, cur = heapq.heappop(q)
    if total > dist[cur]:
        continue
    for next, next_cost in arr[cur]:
        if next_cost + total < dist[next]:
            dist[next] = next_cost + total
            heapq.heappush(q, [next_cost + total, next])
            path[next] = []
            for p in path[cur]:
                path[next].append(p)
            path[next].append(next)
dist[start] = 0

print(dist[end])
print(len(path[end]))
print(' '.join(map(str,path[end])))