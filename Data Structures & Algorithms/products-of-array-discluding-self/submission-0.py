class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        left = 1
        for i, x in enumerate(nums):
            res[i] = left
            left *= x
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        
        return res
