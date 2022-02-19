import heapq
from sys import stdin


class DualPriorityQueue:

    def __init__(self):
        self.max_pq = []
        self.min_pq = []
        self.count = {}

    def insert(self, data):
        heapq.heappush(self.max_pq, -data)
        heapq.heappush(self.min_pq, data)
        if data in self.count:
            self.count[data] += 1
        else:
            self.count[data] = 1

    def pop_max(self):
        while self.max_pq:
            data = -heapq.heappop(self.max_pq)
            if self.count[data] != 0:
                self.count[data] -= 1
                return data
        return None

    def seek_max(self):
        while self.max_pq:
            data = -heapq.heappop(self.max_pq)
            if self.count[data] != 0:
                heapq.heappush(self.max_pq, -data)
                return data
        return None

    def pop_min(self):
        while self.min_pq:
            data = heapq.heappop(self.min_pq)
            if self.count[data] != 0:
                self.count[data] -= 1
                return data
        return None

    def seek_min(self):
        while self.min_pq:
            data = heapq.heappop(self.min_pq)
            if self.count[data] != 0:
                heapq.heappush(self.min_pq, data)
                return data
        return None


t = int(stdin.readline())

for _ in range(t):
    q = DualPriorityQueue()
    k = int(stdin.readline())
    for _ in range(k):
        command = list(stdin.readline().rstrip().split())
        if command[0] == "I":
            q.insert(int(command[1]))
        if command[0] == "D":
            if command[1] == "-1":
                q.pop_min()
            else:
                q.pop_max()
    min_data = q.seek_min()
    max_data = q.seek_max()
    if min_data is None:
        print("EMPTY")
    else:
        print("%d %d" % (max_data, min_data))

