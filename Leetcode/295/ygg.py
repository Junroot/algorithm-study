import heapq


class MedianFinder:
    lq = []
    rq = []

    def __init__(self):
        self.lq = []
        self.rq = []

    def addNum(self, num: int) -> None:
        lq = self.lq
        rq = self.rq

        if 0 == len(lq):
            heapq.heappush(lq, -num)
            return
        if -lq[0] > num:
            heapq.heappush(lq, -num)
        else:
            heapq.heappush(rq, num)

        if len(lq) < len(rq):
            heapq.heappush(lq, -heapq.heappop(rq))
        elif len(rq) < len(lq):
            heapq.heappush(rq, -heapq.heappop(lq))

        # print(lq, rq)

    #         if 1 == len(self.lmh):
    #             self.lmh.append(num)
    #             return

    #         if self.lmh[1] > num:
    #             self.lmh.append(num)
    #             self.maxHeapify(self.lmh)
    #         else:
    #             self.rmh.append(num)
    #             self.minHeapify(self.rmh)

    #         l = len(self.lmh)
    #         r = len(self.rmh)

    #         if l < r:
    #             self.lmh.append(self.rmh[1])
    #             self.maxHeapify(self.lmh)
    #             self.minHeapPop(self.rmh)
    #         elif r < l:
    #             self.rmh.append(self.lmh[1])
    #             self.minHeapify(self.rmh)
    #             self.maxHeapPop(self.lmh)

    # print(self.lmh, self.rmh)

    def findMedian(self) -> float:
        l = len(self.lq)
        r = len(self.rq)

        if l == r:
            return (self.rq[0] - self.lq[0]) / 2
        elif l < r:
            return self.rq[0]
        else:
            return -self.lq[0]

#         l = len(self.lmh)
#         r = len(self.rmh)

#         if l == r:
#             return (self.lmh[1] + self.rmh[1]) / 2
#         elif l < r:
#             return self.rmh[1]
#         else:
#             return self.lmh[1]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()