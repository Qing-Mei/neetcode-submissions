class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for num in nums:
            new_dp = {}

            for total, count in dp.items():
                pos = total + num
                neg = total - num

                new_dp[pos] = new_dp.get(pos, 0) + count
                new_dp[neg] = new_dp.get(neg, 0) + count
            
            dp = new_dp

        return dp.get(target, 0)
        