from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            res = 1

            for j in range(i):
                if nums[i] > nums[j]:
                    res = max(res, 1 + dfs(j))
            
            return res

        return max(dfs(i) for i in range(len(nums)))
