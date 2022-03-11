class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def is_valid_coord(r: int, c: int) -> bool:
            return 0 <= r < row and 0 <= c < col
        
        row, col = len(grid), len(grid[0])
        fresh = 0
        elapsed_time = 0
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        q = collections.deque()
        
        for r in range(row):
            for c in range(col):
                fresh += grid[r][c] % 2
                if grid[r][c] == 2:
                    q.append([r, c])
                    
        while fresh:
            elapsed_time += 1
            is_newly_rotten = False
            for _ in range(len(q)):
                r, c = q.popleft()
                for x, y in move:
                    next_r, next_c = r+x, c+y
                    if is_valid_coord(next_r, next_c) and grid[next_r][next_c] == 1:
                        grid[next_r][next_c] = 2
                        fresh -= 1
                        is_newly_rotten = True
                        q.append([next_r, next_c])
            if not is_newly_rotten:
                return -1
                    
        return elapsed_time
