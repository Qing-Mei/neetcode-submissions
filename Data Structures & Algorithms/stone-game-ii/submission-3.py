class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                if 2 * M >= n - i:
                    dp[i][M] = suffix[i]
                else:
                    for x in range(1, 2 * M + 1):
                        dp[i][M] = max(dp[i][M], suffix[i] - dp[i + x][max(M, x)])

        return dp[0][1]
        