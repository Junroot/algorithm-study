class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        n = len(candies)
        lo, hi = 0, max(candies)
        
        while lo < hi:
            mid = (lo + hi + 1) // 2
            
            piles = 0
            for i in range(n):
                piles += candies[i] // mid
                
            if piles >= k:
                lo = mid
            else:
                hi = mid - 1
            
        return lo
