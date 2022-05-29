from collections import deque
import copy

n, m = map(int, input().split())

arr = [[0 for _ in range(m)]for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, list(input().split())))

ans = -1
for i1 in range(n):
    for j1 in range(m):
        if arr[i1][j1] != 0:
            continue
        for i2 in range(i1, n):
            for j2 in range(m):
                if (i1 == i2 and j1 == j2) or arr[i2][j2] != 0 or (i2 == i1 and j2 < j1):
                    continue
                for i3 in range(i2, n):
                    for j3 in range(m):
                        if (i3 == i1 and j3 == j1) or (i3 == i2 and j3 == j2) or arr[i3][j3] != 0 or (i3 == i2 and j3 < j2):
                            continue
                        arr2 = copy.deepcopy(arr)
                        arr2[i1][j1] = 1
                        arr2[i2][j2] = 1
                        arr2[i3][j3] = 1

                        q = deque()
                        for i in range(n):
                            for j in range(m):
                                if arr[i][j] == 2:
                                    q.append([i, j])

                        while q:
                            y, x = q.pop()

                            if y > 0 and arr2[y-1][x] == 0:
                                arr2[y-1][x] = 2
                                q.append([y-1, x])
                            if y < n - 1 and arr2[y + 1][x] == 0:
                                arr2[y + 1][x] = 2
                                q.append([y + 1, x])
                            if x < m-1 and arr2[y][x+1] == 0:
                                arr2[y][x+1] = 2
                                q.append([y, x+1])
                            if x > 0 and arr2[y][x-1] == 0:
                                arr2[y][x-1] = 2
                                q.append([y, x-1])

                        count = 0
                        for i in range(n):
                            for j in range(m):
                                if arr2[i][j] == 0:
                                    count+=1

                        if count > ans:
                            ans = count
                            a1 = i1
                            b1 = j1
                            a2 = i2
                            b2 = j2
                            a3 = i3
                            b3 = j3

print(ans)
