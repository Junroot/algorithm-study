import sys
n, m = map(int, list(input().split()))

arr = list()
arr_sum = [[0 for _ in range(n)] for _ in range(n)]
question = list()

for _ in range(n):
    line = list(map(int, list(input().split())))
    arr.append(line)

for i in range(n):
    for j in range(n):
        if i == 0:
            if j == 0:
                arr_sum[i][j] = arr[i][j]
            else:
                arr_sum[i][j] = arr_sum[i][j-1] + arr[i][j]
        else:
            if j == 0:
                arr_sum[i][j] = arr_sum[i-1][j] + arr[i][j]
            else:
                arr_sum[i][j] = arr_sum[i-1][j] + arr_sum[i][j-1] - arr_sum[i-1][j-1] + arr[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, list(sys.stdin.readline().split()))
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    ans = 0
    if x1 == 0 and y1 == 0:
        ans = arr_sum[x2][y2]
    elif x1 == 0:
        ans = arr_sum[x2][y2] - arr_sum[x2][y1-1]
    elif y1 == 0:
        ans = arr_sum[x2][y2] - arr_sum[x1-1][y2]
    else:
        ans = arr_sum[x2][y2] - arr_sum[x1-1][y2] - arr_sum[x2][y1-1] + arr_sum[x1-1][y1-1]
    print(ans)