class Solution:
    def rob(self, nums: List[int]) -> int:
        take = 0
        skip = 0

        for num in nums:
            take, skip = skip + num, max(take, skip)

        return max(take, skip)
