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
                end = i + len(word)

                if end <= n and s.startswith(word, i):
                    dp[end] = True
                        
        return dp[n]
