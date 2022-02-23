from collections import deque

m, n = map(int, input().split())

box = []

for i in range(n):
    box.append(list(map(int, input().split())))

queue = deque([])

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])

while queue:
    x, y = queue.popleft()
    day = box[x][y]

    if x < n - 1:
        if box[x + 1][y] == 0:
            box[x + 1][y] = day + 1
            queue.append([x + 1, y])
    if y < m - 1:
        if box[x][y + 1] == 0:
            box[x][y + 1] = day + 1
            queue.append([x, y + 1])
    if x > 0:
        if box[x - 1][y] == 0:
            box[x - 1][y] = day + 1
            queue.append([x - 1, y])
    if y > 0:
        if box[x][y - 1] == 0:
            box[x][y - 1] = day + 1
            queue.append([x, y - 1])

#print(box)

ans = 0
IsEnd = 1

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            IsEnd = 0
        else:
            ans = max(box[i][j], ans)

if IsEnd == 0:
    print(-1)
else:
    print(ans - 1)