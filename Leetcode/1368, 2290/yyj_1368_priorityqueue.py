class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        def is_valid_coord(r: int, c: int) -> bool:
            return 0 <= r < M and 0 <= c < N
        
        M, N = len(grid), len(grid[0])
        pq = []
        move = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        dist = [[math.inf] * N for _ in range(M)]
        
        dist[0][0] = 0
        heapq.heappush(pq, [dist[0][0], 0, 0, grid[0][0]])
        
        while pq:
            cost, r, c, direction = heapq.heappop(pq)
            if r == M-1 and c == N-1:
                return cost
            
            for mv in move:
                expense = 0 if direction == mv else 1
                dy, dx = move[mv]
                nr, nc = r+dy, c+dx
                if is_valid_coord(nr, nc) and cost + expense < dist[nr][nc]:
                    dist[nr][nc] = cost + expense
                    heapq.heappush(pq, [cost + expense, nr, nc, grid[nr][nc]])
                    
        return dist[M-1][N-1]
