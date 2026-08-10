class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        m = len(text1)
        n = len(text2)

        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            prev = 0

            for j in range(1, n + 1):
                old_dp_j = dp[j]

                if text1[i - 1] == text2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                
                prev = old_dp_j
        
        return dp[n]
