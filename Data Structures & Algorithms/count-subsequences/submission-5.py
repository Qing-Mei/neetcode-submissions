class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(m - 1, -1, -1):
            prev = 1
            for j in range(n - 1, -1, -1):
                old_j = dp[j] # before update, dp[i + 1][j]
                if s[i] == t[j]:
                    dp[j] += prev
                prev = old_j # prev = dp[i + 1][j] next_j = j - 1
        
        return dp[0]
