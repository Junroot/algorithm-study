TC = int(input())

for i in range(TC):
    n, m, w = map(int, input().split())
    nodes = [[] for _ in range(n+1)]
    dist = [10001 for _ in range(n+1)]
    for i in range(m):
        s, e, t = map(int, input().split())
        nodes[s].append([e, t])
        nodes[e].append([s, t])
    for i in range(w):
        s, e, t = map(int, input().split())
        nodes[s].append([e, -t])

    #bellman-ford
    dist[1] = 0
    IsLoop = 0
    for i in range(1, n+1):
        for cur in range(1, n+1):
            for next, time in nodes[cur]:
                if dist[cur] + time < dist[next]:
                    dist[next] = dist[cur] + time
                    if i == n:
                        IsLoop = 1
    if IsLoop == 1:
        print("YES")
    else:
        print("NO")