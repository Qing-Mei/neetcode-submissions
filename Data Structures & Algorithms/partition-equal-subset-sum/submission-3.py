class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total & 1:
            return False
        
        half = total // 2
        n = len(nums)

        dp = [False] * (half + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(half, nums[i - 1] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i - 1]]
        
        return dp[half]
