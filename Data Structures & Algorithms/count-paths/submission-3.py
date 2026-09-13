class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n
        dp[0] = 1

        for i in range(m):
            dp[0] = 1
            for j in range(1, n):
                dp[j] += dp[j - 1]
        
        return dp[n - 1]
