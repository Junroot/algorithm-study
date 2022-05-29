class Union_Find:
    def __init__(self, size: int) -> None:
        self.root = [[[r, c] for c in range(size)] for r in range(size)]
        self.rank = [[1] * size for _ in range(size)]
        
    def find(self, x: List[int]) -> List[int]:
        r, c = x
        if x == self.root[r][c]:
            return x
        self.root[r][c] = self.find(self.root[r][c])
        return self.root[r][c]
    
    def union(self, x: List[int], y: List[int]) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            xr, xc = root_x
            yr, yc = root_y
            if self.rank[xr][xc] > self.rank[yr][yc]:
                self.root[yr][yc] = root_x
            elif self.rank[xr][xc] < self.rank[yr][yc]:
                self.root[xr][xc] = root_y
            else:
                self.root[yr][yc] = root_x
                self.rank[xr][xc] += 1
    
    def connected(self, x: List[int], y: List[int]) -> bool:
        return self.find(x) == self.find(y)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        def is_valid_coord(r: int, c: int) -> bool:
            return 0 <= r < N and 0 <= c < N
        
        N = len(grid)
        if N == 1:
            return 0
        
        start = [0, 0]
        goal = [N-1, N-1]
        pq = []
        is_activated = [[False] * N for _ in range(N)]
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for r in range(N):
            for c in range(N):
                pq.append([grid[r][c], [r, c]])
        
        heapq.heapify(pq)
        
        uf = Union_Find(N)
        while not uf.connected(start, goal):
            t, coord = heapq.heappop(pq)
            r, c = coord
            is_activated[r][c] = True
            for dy, dx in move:
                nr, nc = r+dy, c+dx
                if is_valid_coord(nr, nc) and is_activated[nr][nc]:
                    uf.union([r, c], [nr, nc])
        
        return t
