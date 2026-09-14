class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = list(range(n + 1))
        
        for i in range(1, m + 1):
            prev = i - 1
            dp[0] = i

            for j in range(1, n + 1):
                old_dp_j = dp[j]

                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = 1 + min(dp[j - 1], dp[j], prev)
                    
                prev = old_dp_j
        
        return dp[n]
