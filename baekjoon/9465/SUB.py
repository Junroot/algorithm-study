t = int(input())
for _ in range(t):
    n = int(input())
    arr = [[] for _ in range(2)]
    arr[0] = list(map(int, list(input().split())))
    arr[1] = list(map(int, list(input().split())))

    for j in range(1, n):
        for i in range(2):
            if i == 0:
                if j == 1:
                    arr[i][j] += arr[i+1][j-1]
                else:
                    arr[i][j] += max(arr[i+1][j-1], arr[i+1][j-2])
            else:
                if j == 1:
                    arr[i][j] += arr[i-1][j-1]
                else:
                    arr[i][j] += max(arr[i-1][j-1], arr[i-1][j-2])
    #print(arr)
    print(max(arr[0][n-1],arr[1][n-1]))