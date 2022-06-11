class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        def is_valid_coord(r: int, c: int) -> bool:
            return 0 <= r < M and 0 <= c < N
        
        M, N = len(grid), len(grid[0])
        dist = [[math.inf] * N for _ in range(M)]
        deque = collections.deque()
        move = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        
        dist[0][0] = 0
        deque.appendleft( [dist[0][0], 0, 0, grid[0][0]] )
        
        while deque:
            cost, r, c, direction = deque.popleft()
            for d in move:
                dy, dx = move[d]
                nr, nc = r+dy, c+dx
                expense = 0 if d == direction else 1
                if is_valid_coord(nr, nc) and dist[r][c] + expense < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + expense
                    if not expense:
                        deque.appendleft( [dist[nr][nc], nr, nc, grid[nr][nc]] )
                    else:
                        deque.append( [dist[nr][nc], nr, nc, grid[nr][nc]] )
                        
        return dist[M-1][N-1]
