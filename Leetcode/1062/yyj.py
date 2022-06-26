class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        
        def is_there_duplicate(length: int) -> bool:
            if not length:
                return True
            if length > N:
                return False
            
            subs = set()
            for i in range(N-length+1):
                sub = s[i:i+length]
                if sub in subs:
                    return True
                else:
                    subs.add(sub)
            return False
        
        
        N = len(s)
        lo, hi = 0, N
        
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if is_there_duplicate(mid):
                lo = mid
            else:
                hi = mid - 1
        
        return lo
