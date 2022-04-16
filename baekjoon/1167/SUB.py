from collections import deque

n = int(input())
arr = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
visit2 = [0 for _ in range(n+1)]

for i in range(n):
    temp = list(map(int, input().split()))
    node_num = temp[0]
    for j in range(1, len(temp)-1):
        if j%2 == 1:
            arr[node_num].append([temp[j], temp[j+1]])

q = deque()
q.append([1, 0])
visit[1] = 1

max_node = 1
max_len = 0
#print(arr)
while q:
    cur, len = q.popleft()
    #print(cur, len)
    if len > max_len:
        max_len = len
        max_node = cur

    for e in arr[cur]:
        if visit[e[0]] == 0:
            visit[e[0]] = 1
            q.append([e[0], len+e[1]])

#print(max_node, max_len)

q.append([max_node, 0])
visit2[max_node] = 1
max_node = 1
max_len = 0
#print(arr)
while q:
    cur, len = q.popleft()
    #print(cur, len)
    if len > max_len:
        max_len = len
        max_node = cur

    for e in arr[cur]:
        if visit2[e[0]] == 0:
            visit2[e[0]] = 1
            q.append([e[0], len + e[1]])

print(max_len)