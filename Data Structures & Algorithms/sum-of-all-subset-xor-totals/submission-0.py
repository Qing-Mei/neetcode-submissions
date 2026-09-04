class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i, xor_sum):
            if i == n:
                return xor_sum

            include = dfs(i + 1, xor_sum ^ nums[i])
            exclude = dfs(i + 1, xor_sum)

            return include + exclude
        
        return dfs(0, 0)
