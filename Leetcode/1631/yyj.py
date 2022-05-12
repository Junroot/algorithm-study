class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def is_valid_vertex(r: int, c: int) -> bool:
            return 0 <= r < row and 0 <= c < col
        
        row, col = len(heights), len(heights[0])
        start, end = (0, 0), (row-1, col-1)
        adj_move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        not_visited = set()
        minheap = []
        max_effort = collections.defaultdict(int)
        connections = collections.defaultdict(list)
        
        for r in range(row):
            for c in range(col):
                max_effort[(r, c)] = 0 if (r, c) == start else sys.maxsize
                not_visited.add((r, c))
                for dy, dx in adj_move:
                    nr, nc = r+dy, c+dx
                    if is_valid_vertex(r+dy, c+dx):
                        effort = abs(heights[nr][nc] - heights[r][c])
                        connections[(r, c)].append([(nr, nc), effort])
        
        heapq.heappush(minheap, [max_effort[start], start])
        while minheap and not_visited:
            effort, src = heapq.heappop(minheap)
            if src not in not_visited:
                continue
            for dest, effort in connections[src]:
                curr_max_effort = max(effort, max_effort[src])
                if max_effort[dest] > curr_max_effort:
                    max_effort[dest] = curr_max_effort
                    heapq.heappush(minheap, [max_effort[dest], dest])
            not_visited.remove(src)
            
        return max_effort[end]
