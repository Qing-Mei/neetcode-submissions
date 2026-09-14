class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_res = nums[0]
        curr = nums[0]

        for i in range(1, len(nums)):
            curr = max(0, curr) + nums[i]
            max_res = max(max_res, curr)
        
        return max_res
