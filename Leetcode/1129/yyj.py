class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        res = [-1 for _ in range(n)]
        res[0] = 0
        var = 2
        
        colormap = [collections.defaultdict(set) for i in range(var)]
        edges = [redEdges, blueEdges]
        for color in range(var):
            for src, dest in edges[color]:
                colormap[color][src].add(dest)
        
        q = collections.deque()
        visited_edges = set()
        for color in range(var):
            for node in colormap[color][0]:
                visited_edges.add((0, node, color))
                q.append([node, color, 1])
            
        while q:
            node, color, length = q.popleft()
            if res[node] == -1:
                res[node] = length
            color = (color + 1) % var
            for n_node in colormap[color][node]:
                if (node, n_node, color) not in visited_edges:
                    visited_edges.add((node, n_node, color))
                    q.append([n_node, color, length + 1])

        return res
