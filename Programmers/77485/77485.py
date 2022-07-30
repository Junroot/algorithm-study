import sys

def solution(rows, columns, queries):
    def is_valid_coord(x: int, y: int) -> bool:
        return x1 <= x <= x2 and y1 <= y <= y2
    
    matrix = [[(r*columns + c+1) for c in range(columns)] for r in range(rows)]
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    res = []
    
    for q in queries:
        x1, y1, x2, y2 = [idx-1 for idx in q]
        r, c = x1, y1
        prev, cur = 0, matrix[r][c]
        min_moved = sys.maxsize
        m = 0
        
        while cur != 0:
            cur = matrix[r][c]
            matrix[r][c] = prev
            if cur != 0 and cur < min_moved:
                min_moved = cur
            prev = cur
            dy, dx = move[m]
            if not is_valid_coord(r+dy, c+dx):
                m = (m + 1) % 4
                dy, dx = move[m]
            r, c = r+dy, c+dx
            
        res.append(min_moved)
            
    return res
