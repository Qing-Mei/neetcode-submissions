class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True


        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                if p[j] == "*":
                    continue

                match = i < m and (s[i] == p[j] or p[j] == ".")

                if j + 1 < n and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or match and dp[i + 1][j]
                else:
                    dp[i][j] = match and dp[i + 1][j + 1]
        
        return dp[0][0]
        