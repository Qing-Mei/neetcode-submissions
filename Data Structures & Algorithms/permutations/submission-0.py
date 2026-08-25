class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(start):
            if start == n:
                res.append(nums[:])
                return
            
            for i in range(start, n):
                nums[i], nums[start] = nums[start], nums[i]
                dfs(start + 1)
                nums[i], nums[start] = nums[start], nums[i]
        
        dfs(0)

        return res
