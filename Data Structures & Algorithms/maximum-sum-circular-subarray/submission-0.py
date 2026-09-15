class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)

        curr_max = max_sub = nums[0]
        curr_min = min_sub = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            curr_max = max(curr_max, 0) + x
            max_sub = max(max_sub, curr_max)
            
            curr_min = min(curr_min, 0) + x
            min_sub = min(min_sub, curr_min)
        
        if max_sub < 0:
            return max_sub
        
        return max(max_sub, total - min_sub)
