class CountIntervals:
    vals = []
    cnt = 0

    def __init__(self):
        self.vals = []
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        i = 0

        # TLE
        if i >= len(self.vals) or self.vals[-1][1] < left:
            self.cnt += right - left + 1
            self.vals.append([left, right])

        while i < len(self.vals):
            if left > self.vals[i][1]:
                i += 1
                continue
            if right < self.vals[i][0]:
                self.cnt += right - left + 1
                self.vals.insert(i, [left, right])
                return

            if left < self.vals[i][0]:
                self.cnt += self.vals[i][0] - left
                self.vals[i][0] = left
            if self.vals[i][1] <= right:
                i += 1
                last = 0
                # WA, add equal
                while i < len(self.vals) and self.vals[i][0] <= right:
                    self.cnt -= self.vals[i][1] - self.vals[i][0] + 1
                    last = self.vals.pop(i)[1]
                i -= 1
                m = max(right, last)
                self.cnt += m - self.vals[i][1]
                self.vals[i][1] = m
            return

        if i >= len(self.vals):
            self.vals.append([left, right])
            self.cnt += right - left + 1
            return

    def count(self) -> int:
        return self.cnt

# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()


ci = CountIntervals()
ci.add(2, 3)
ci.add(7, 10)
print(ci.count())
ci.add(5, 8)
print(ci.count())
