import sys

def solution(s):
    min_length = sys.maxsize
    N = len(s)
    
    for unit in range(1, N+1):
        res = ""
        prev = ""
        freq = 1
        
        for pos in range(0, N+unit, unit):
            cur = s[pos:pos+unit]
            if prev == cur:
                freq += 1
            elif (prev and prev != cur):
                res += prev if freq == 1 else (str(freq)+prev)
                freq = 1
            prev = cur
        
        length = len(res)
        
        if length < min_length:
            min_length = length
    
    return min_length
