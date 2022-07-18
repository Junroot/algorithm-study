class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        @lru_cache(None)
        def finder(i: int, remain: int) -> bool:
            if not remain:
                return True
            if i == N or remain < 0:
                return False
            
            result = finder(i+1, remain-nums[i]) or finder(i+1, remain)
            
            return result
            
        
        S = sum(nums)
        N = len(nums)
        if N <= 1 or S % 2 == 1:
            return False
        
        target = S // 2
        
        return finder(0, target)
