class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res = nums[0]

        curr = nums[0]

        for i in range(1, len(nums)):
            curr = max(curr + nums[i], nums[i])

            res = max(res, curr)
        
        return res
