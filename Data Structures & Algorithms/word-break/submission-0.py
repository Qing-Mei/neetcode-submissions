class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)

        dp[0] = True

        i = 0

        for i in range(n):
            if not dp[i]:
                continue

            for word in wordDict:
                l = len(word)

                if i + l <= n and s[i:i + l] == word:
                    dp[i + l] = True
                        
        return dp[n]
