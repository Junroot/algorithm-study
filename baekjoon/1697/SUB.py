from collections import deque

n, m = map(int, list(input().split()))
arr = [0] * 100002
ans = 0

q = deque()

q.append(n)

while q:
    cur = q.popleft()

    if cur == m:
        print(arr[cur])
        break

    for el in (cur-1, cur+1, cur*2):
        if 0 <= el <= 100001 and not arr[el]:
            arr[el] = arr[cur] + 1
            q.append(el)