from collections import deque

n, k = map(int, input().split())
arr = [[0, 0] for _ in range(150000)]
ans = 0
ans_num = 0

q = deque()
arr[n][1] = 1
q.append(n)

while q:
    cur = q.popleft()
    #print(arr[cur], cur)

    if cur == k:
        ans = cur
        break

    if ans == 0:
        for i in (cur - 1, cur + 1, cur * 2):
            if 0 <= i <= 140000:
                if arr[i][0] == 0:
                    arr[i][0] = arr[cur][0] + 1
                    arr[i][1] = arr[cur][1]
                    q.append(i)
                elif arr[cur][0] != 0 and arr[cur][0] + 1 == arr[i][0]:
                    arr[i][1] += arr[cur][1]

print(arr[ans][0])
print(arr[ans][1])