class Solution:
    @cache
    def check(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True
    
    #@cache # cache is shallow copy
    def comb(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]
        
        ans = []
        for i in range(1, len(s)):
            if False == self.check(s[:i]):
                continue
            
            cand = self.comb(s[i:])
            for j in range(len(cand)):
                cand[j] = [s[:i]] + cand[j]
                
            ans += cand
            
        if self.check(s):
            ans += [[s]]
        
        return ans
    
    def partition(self, s: str) -> List[List[str]]:
        return self.comb(s)

        
