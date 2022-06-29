import sys
import heapq
n, k = map(int, input().split())

ans = 0
jewel = []
bag = []
max_value = []
heapq.heapify(jewel)
heapq.heapify(bag)
heapq.heapify(max_value)

for i in range(n):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(jewel, [m, v])

for i in range(k):
    c = int(sys.stdin.readline())
    heapq.heappush(bag, c)

for i in range(k):
    bag_weight = heapq.heappop(bag)

    while jewel:
        if bag_weight >= jewel[0][0]:
            heapq.heappush(max_value, -1*(jewel[0][1]))
            heapq.heappop(jewel)
        else:
            break

    if len(max_value) > 0:
        ans+=-1*max_value[0]
        heapq.heappop(max_value)


print(ans)