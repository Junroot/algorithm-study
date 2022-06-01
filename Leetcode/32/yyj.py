class Solution:
    def longestValidParentheses(self, s: str) -> int:
        N = len(s)
        left_p, right_p = '(', ')'
        res = 0
        left, right = 0, 0
        
        for p in s:
            if p == left_p:
                left += 1
            elif p == right_p:
                right += 1
            
            if left == right:
                res = max(res, left * 2)
            elif left < right:
                left, right = 0, 0
        
        left, right = 0, 0
        for p in reversed(s):
            if p == left_p:
                left += 1
            elif p == right_p:
                right += 1
            
            if left == right:
                res = max(res, left * 2)
            elif left > right:
                left, right = 0, 0
                
        return res
