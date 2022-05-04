from collections import deque

n, k = map(int, input().split())
arr = [-1] * 100003
ans = 0

q = deque()
q.append(n)
arr[n] = 0

while q:
    cur = q.popleft()

    if cur == k:
        ans = arr[cur]
        break

    if 0 <= cur*2 <= 100001 and arr[cur*2] == -1:
        arr[cur*2] = arr[cur]
        q.appendleft(cur*2)
    if 0 <= cur - 1 <= 100001 and arr[cur - 1] == -1:
        arr[cur - 1] = arr[cur] + 1
        q.append(cur - 1)
    if 0 <= cur+1 <= 100001 and arr[cur+1] == -1:
        arr[cur+1] = arr[cur]+1
        q.append(cur+1)



print(arr[k])
