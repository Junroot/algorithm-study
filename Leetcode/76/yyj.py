class Solution:
    def minWindow(self, s: str, t: str) -> str:
        remain = len(t)
        t_counter = collections.Counter(t)
        
        res = ''
        maxlen = sys.maxsize        
        l = 0
        for r, r_char in enumerate(s):
            t_counter[r_char] -= 1
            if t_counter[r_char] >= 0:
                remain -= 1
                
            if not remain:
                while l < r:
                    l_char = s[l]
                    if t_counter[l_char] < 0:
                        t_counter[l_char] += 1
                        l += 1
                    else:
                        break
                
                currlen = r - l + 1
                if currlen < maxlen:
                    maxlen = currlen
                    res = s[l : r+1]
            
        return res
