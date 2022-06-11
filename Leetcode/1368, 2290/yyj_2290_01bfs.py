class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        def is_valid_coord(r: int, c: int) -> bool:
            return 0 <= r < M and 0 <= c < N
        
        M, N = len(grid), len(grid[0])
        deque = collections.deque()
        min_cost = [[math.inf] * N for _ in range(M)]
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        min_cost[0][0] = 0
        deque.appendleft( [0, 0, min_cost[0][0]] )
        
        while deque:
            r, c, cost = deque.popleft()
            for dy, dx in move:
                nr, nc = r+dy, c+dx
                if is_valid_coord(nr, nc) and cost + grid[nr][nc] < min_cost[nr][nc]:
                    min_cost[nr][nc] = cost + grid[nr][nc]
                    if not grid[nr][nc]:
                        deque.appendleft( [nr, nc, min_cost[nr][nc]] )
                    else:
                        deque.append( [nr, nc, min_cost[nr][nc]] )
                            
        return min_cost[M-1][N-1]
