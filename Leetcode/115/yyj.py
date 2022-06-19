class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def finder(ps: int, pt: int) -> int:
            if pt == T:
                return 1
            if S-ps < T-pt:
                return 0
            
            res = 0
            for i in range(ps, S):
                if s[i] == t[pt]:
                    if (i+1, pt+1) not in cache:
                        cases = finder(i+1, pt+1)
                        cache[(i+1, pt+1)] = cases
                    res += cache[(i+1, pt+1)]
            
            return res
            
        
        S, T = len(s), len(t)
        cache = {}
        
        return finder(0, 0)
