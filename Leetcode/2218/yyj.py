class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @lru_cache(None)
        def pick(pile_idx: int, need_to_pick: int) -> int:
            if pile_idx == n or need_to_pick == 0:
                return 0
            
            res = pick(pile_idx+1, need_to_pick)    # set default value: pick nothing in pile[pile_idx]
            curr_total = 0
            for j in range(min(len(piles[pile_idx]), need_to_pick)):
                curr_total += piles[pile_idx][j]
                res = max(res, curr_total + pick(pile_idx+1, need_to_pick-j-1))
            return res
        
        n = len(piles)
        
        return pick(0, k)
