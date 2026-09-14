class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        dp = [[(0, 0)] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = (piles[i], 0)
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                other1, mine1 = dp[i + 1][j]
                other2, mine2 = dp[i][j - 1]

                if piles[i] + mine1 > piles[j] + mine2:
                    dp[i][j] = (piles[i] + mine1, other1)
                else:
                    dp[i][j] = (piles[j] + mine2, other2)
            
        alice, bob = dp[0][n - 1]

        return alice > bob
        