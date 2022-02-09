from collections import deque
from sys import stdin

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
m, n = map(int, stdin.readline().split())
graph = [stdin.readline().strip().split() for _ in range(n)]
q = deque()
left = 0

for y in range(n):
    for x in range(m):
        if graph[y][x] == "0":
            left += 1
        if graph[y][x] == "1":
            q.append((x, y, 0))

latest_day = 0

while q:
    x, y, day = q.popleft()
    latest_day = day
    for direction in directions:
        new_x = x + direction[0]
        new_y = y + direction[1]
        if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
            continue
        if graph[new_y][new_x] == "0":
            graph[new_y][new_x] = "1"
            left -= 1
            q.append((new_x, new_y, day + 1))

if left > 0:
    print("-1")
else:
    print(latest_day)
