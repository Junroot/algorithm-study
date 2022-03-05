from collections import defaultdict
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts_per_number = defaultdict(int)

        for num in nums:
            counts_per_number[num] += 1

        if len(counts_per_number.keys()) == 1:
            return nums[0] * len(nums)

        max_number = max(counts_per_number.keys())

        maximum_sum_to_number = [0 for _ in range(max_number + 1)]
        maximum_sum_to_number[1] = counts_per_number[1]
        maximum_sum_to_number[2] = counts_per_number[2]

        for i in range(2, max_number + 1):
            maximum_sum_to_number[i] = max(maximum_sum_to_number[i - 2] + counts_per_number[i] * i,
                                           maximum_sum_to_number[i - 1])

        return maximum_sum_to_number[max_number]
