class Solution:
    def rob(self, nums: List[int]) -> int:
        take = 0
        skip = 0

        for money in nums:
            take, skip = skip + money, max(take, skip)

        return max(take, skip)
