from functools import cache

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # total 1 weight: s 2 weight: total - s
        # total - s - s
        # total = 2s
        # s = total // 2
        # target = total // 2

        total = sum(stones)
        target = total // 2
        n = len(stones)

        @cache
        def dfs(i, remain):
            if i == n or remain == 0:
                return 0
            
            best = dfs(i + 1, remain)

            if stones[i] <= remain:
                best = max(best, stones[i] + dfs(i + 1, remain - stones[i]))
            
            return best
        
        return total - 2 * dfs(0, target)
