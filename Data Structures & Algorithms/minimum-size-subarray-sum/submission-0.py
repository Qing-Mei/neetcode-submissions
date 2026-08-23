class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        res = len(nums) + 1

        for r, num in enumerate(nums):
            total += num

            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
            
        return 0 if res == len(nums) + 1 else res
        