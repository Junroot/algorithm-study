class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minheap = []
        used_bricks_if_reach_building_i = 0
        
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            
            #diff <= 0 : no restriction, just move to the next building
            
            if diff > 0:
                if len(minheap) < ladders:
                    heapq.heappush(minheap, diff)
                else:
                    if minheap and diff > minheap[0]:
                        usebrick = heapq.heapreplace(minheap, diff)
                        used_bricks_if_reach_building_i += usebrick
                    else:
                        used_bricks_if_reach_building_i += diff
                        
                if used_bricks_if_reach_building_i > bricks:
                    return i
        
        return len(heights)-1
