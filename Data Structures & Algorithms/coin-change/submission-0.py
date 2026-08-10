class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for curr in range(1, amount + 1):
            for coin in coins:
                if curr >= coin:
                    dp[curr] = min(dp[curr], dp[curr - coin] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1
