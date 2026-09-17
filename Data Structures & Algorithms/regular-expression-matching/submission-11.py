class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(m, -1, -1):
            prev = dp[n]
            dp[n] = (i == m)

            for j in range(n - 1, -1, -1):
                old_j = dp[j]

                if p[j] != "*":
                    match = i < m and (s[i] == p[j] or p[j] == ".")

                    if j + 1 < n and p[j + 1] == "*":
                        dp[j] = dp[j + 2] or match and dp[j]
                    else:
                        dp[j] = match and prev
                    
                    prev = old_j
        
        return dp[0]
