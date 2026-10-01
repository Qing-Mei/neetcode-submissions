class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        l = 0
        min_length = len(nums) + 1

        for r, num in enumerate(nums):
            total += num

            while total >= target:
                min_length = min(min_length, r - l + 1)

                total -= nums[l]
                l += 1
            
        return 0 if min_length == len(nums) + 1 else min_length
        