class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mem = {}
        
        def dp(remaining_dice: int, remaining_sum: int) -> int:
            if remaining_dice == 0:
                return 1 if remaining_sum == 0 else 0
            elif remaining_sum <= 0:
                return 0
            
            if (remaining_dice, remaining_sum) in mem:
                return mem[(remaining_dice, remaining_sum)]
            
            res = 0
            for face in range(1, k+1):
                res += dp(remaining_dice-1, remaining_sum-face)
            mem[(remaining_dice, remaining_sum)] = res
            return res
        
        modulo = pow(10, 9) + 7
        return dp(n, target) % modulo
