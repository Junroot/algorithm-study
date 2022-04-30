class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles = sorted(rectangles, key = lambda x: (x[0], x[1]))
        np = len(points)
        res = [0 for _ in range(np)]
        
        rec_y_maps = [[] for _ in range(101)]
        for x, y in rectangles:
            rec_y_maps[y].append(x)
            
        for i, coord in enumerate(points):
            cur = 0
            for j in range(coord[1], 101):
                if rec_y_maps[j]:
                    cur += len(rec_y_maps[j])-bisect.bisect_left(rec_y_maps[j], coord[0])
            res[i] = cur
            
        return res
