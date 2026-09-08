from functools import cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        @cache
        def dfs(target):
            if target == 0:
                return 1
            
            count = 0
            
            for num in nums:
                if num > target:
                    break

                count += dfs(target - num)
        
            return count
        
        return dfs(target)
        