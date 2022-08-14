from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)

        if l == 1 or k == 1:
            return nums

        dq = deque()
        dq.append(nums[0])

        for n in nums[1:k]:
            while dq and n > dq[-1]:
                dq.pop()

            if not dq or n > dq[0]:
                dq.appendleft(n)
            else:
                dq.append(n)

        ans = [dq[0]]
        for i in range(k, l):
            n = nums[i]

            if dq and nums[i - k] == dq[0]:
                dq.popleft()

            while dq and n > dq[-1]:
                dq.pop()

            if not dq or n > dq[0]:
                dq.appendleft(n)
            else:
                dq.append(n)

            ans.append(dq[0])

        return ans

#         # TLE
#         l = len(nums)

#         if l == 1 or k == 1:
#             return nums

#         ans = [0] * l
#         for i, n in enumerate(nums):
#             for j in range(k):
#                 if i - j >= 0 and n >= nums[i - j]:
#                     ans[i - j] = n
#                 else:
#                     break

#         return ans[:-(k-1)]