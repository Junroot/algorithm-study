import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        costs = [0]
        pq = []

        for i in range(1, len(heights)):
            difference = heights[i] - heights[i - 1]
            if difference <= 0:
                costs.append(costs[i - 1])
                continue

            heapq.heappush(pq, difference)
            if len(pq) <= ladders:
                costs.append(0)
                continue

            min_difference = heapq.heappop(pq)
            costs.append(costs[i - 1] + min_difference)
            if costs[i] > bricks:
                return i - 1

        return len(heights) - 1

