from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dfs(i, remain):
            if i == n:
                return 1 if remain == 0 else 0
            
            return dfs(i + 1, remain - nums[i]) + dfs(i + 1, remain + nums[i])
        
        return dfs(0, target)
