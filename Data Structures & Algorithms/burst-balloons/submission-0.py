from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @cache
        def dfs(l, r):
            if l > r:
                return 0
            
            best = 0

            for i in range(l, r + 1):
                coins = nums[i] * nums[l - 1] * nums[r + 1]

                best = max(best, coins + dfs(l, i - 1) + dfs(i + 1, r))

            return best
        
        return dfs(1, len(nums) - 2)
