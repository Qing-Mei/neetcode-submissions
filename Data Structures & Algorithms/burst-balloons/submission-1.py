class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        n = len(nums)
        dp = [[0] * (n) for _ in range(n)]

        for l in range(n - 2, 0, -1):
            for r in range(l, n - 1):
                coins = nums[l - 1] * nums[r + 1]

                for i in range(l, r + 1):
                    dp[l][r] = max(dp[l][r], dp[l][i - 1] + coins * nums[i] + dp[i + 1][r])
        
        return dp[1][n - 2]
