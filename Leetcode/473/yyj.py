class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        @lru_cache(None)
        def finder(i, s1, s2, s3, s4) -> bool:
            if i == N:
                return s1 == s2 == s3 == s4
            
            return ( s1+matchsticks[i] <= target and finder(i+1, s1+matchsticks[i], s2, s3, s4)
                or s2+matchsticks[i] <= target and finder(i+1, s1, s2+matchsticks[i], s3, s4)
                or s3+matchsticks[i] <= target and finder(i+1, s1, s2, s3+matchsticks[i], s4)
                or s4+matchsticks[i] <= target and finder(i+1, s1, s2, s3, s4+matchsticks[i]) )
        
        
        N = len(matchsticks)
        S = sum(matchsticks)
        target = S // 4
        
        if N < 4 or S % 4:
            return False
        for stick in matchsticks:
            if stick > target:
                return False
        
        matchsticks = sorted(matchsticks, reverse=True)
        
        return finder(0, 0, 0, 0, 0)
