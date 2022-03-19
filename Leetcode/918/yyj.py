class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        dp_contiguous = [0 for _ in range(n)]
        max_contiguous = -sys.maxsize
        
        dp_excluding_both_ends = [0 for _ in range(n)]
        min_excluding_both_ends = sys.maxsize
        
        for i in range(n):
            dp_contiguous[i] = max(nums[i]+dp_contiguous[i-1], nums[i])
            max_contiguous = max(max_contiguous, dp_contiguous[i])
            
        for i in range(1, n-1):
            dp_excluding_both_ends[i] = min(nums[i]+dp_excluding_both_ends[i-1], nums[i])
            min_excluding_both_ends = min(min_excluding_both_ends, dp_excluding_both_ends[i])
        max_splited = sum(nums) - min_excluding_both_ends
        
        return max(max_contiguous, max_splited)
