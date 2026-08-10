class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(nums, path, start, target):
            if target == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(nums)):
                num = nums[i]
                
                if num > target:
                    continue

                path.append(num)

                dfs(nums, path, i, target - num)

                path.pop()
        
        dfs(nums, [], 0, target)

        return res
