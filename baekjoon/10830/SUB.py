n, b = map(int, input().split())
arr = [[[0 for _ in range(n)]for _ in range(n)] for _ in range(37)]
ans = [[1 for _ in range(n)] for _ in range(n)]
for i in range(n):
    arr[0][i] = list(map(int, input().split()))

for num in range(1,37):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                arr[num][i][j] += (arr[num-1][i][k] * arr[num-1][k][j]) % 1000

cur = (1<<36)
cur_num = 36
print(cur)
while(True):
    if b > cur:
        temp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    temp[i][j] += (ans[i][k] * arr[cur_num][k][j]) % 1000
        ans = temp.copy()

    cur = cur>>1
    cur_num-=1
    if cur_num < 0:
        break

print(ans)