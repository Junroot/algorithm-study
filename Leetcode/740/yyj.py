class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        scores = [0 for i in range(10001)]
        for n in c:
            scores[n] = n * c[n]
        
        def dp(n):
            if n < 2:
                return max(scores[:n+1])
            if n not in mem:
                mem[n] = max(dp(n-1), dp(n-2)+scores[n])
            return mem[n]
        
        mem = {}
        
        return dp(len(scores)-1)
