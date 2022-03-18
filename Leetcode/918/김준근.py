from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [nums[0]]

        for i in range(1, len(nums)):
            dp.append(max(dp[-1] + nums[i], nums[i]))

        result = max(dp)

        dp = [nums[1]]

        for i in range(2, len(nums) - 1):
            dp.append(min(nums[i], dp[-1] + nums[i]))

        result = max(result, sum(nums) - min(dp))

        return result


print(Solution().maxSubarraySumCircular([5,5,0,-5,3,-3,2]))
