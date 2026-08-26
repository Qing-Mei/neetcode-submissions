class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(i):
            if i == n:
                res.append(nums[:])
                return

            used = set()

            for j in range(i, n):
                if nums[j] in used:
                    continue
                
                used.add(nums[j])

                nums[j], nums[i] = nums[i], nums[j]
                dfs(i + 1)
                nums[j], nums[i] = nums[i], nums[j]

        dfs(0)
        return res
