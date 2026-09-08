class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total & 1:
            return False
        
        half = total // 2
        n = len(nums)

        dp = [[False] * (half + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True
        
        for i in range(1, n + 1):
            for j in range(1, half + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n - 1][half]
