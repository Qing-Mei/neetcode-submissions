class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total & 1:
            return False
        
        half = total // 2

        dp = [False] * (half + 1)
        dp[0] = True

        for num in nums:
            for s in range(half, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]
        
        return dp[half]
        