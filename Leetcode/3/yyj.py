class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        res = 0
        
        unimap = {}
        for i in range(128):
            unimap[i] = 0
        
        while right < len(s):
            r = s[right]
            unimap[ord(r)] += 1
            
            while unimap[ord(r)] > 1:
                l = s[left]
                unimap[ord(l)] -= 1
                left += 1
            
            res = max(res, right-left+1)
        
            right += 1
            
        return res
