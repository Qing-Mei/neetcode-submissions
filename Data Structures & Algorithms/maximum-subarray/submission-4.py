class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * n
        dp[n - 1] = nums[n - 1]
        res = nums[n - 1]

        for i in range(n - 2, -1, -1):
            dp[i] = max(nums[i], nums[i] + dp[i + 1])
            res = max(res, dp[i])
        
        return res
