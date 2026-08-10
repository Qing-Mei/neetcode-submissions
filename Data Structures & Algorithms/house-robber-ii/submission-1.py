class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        take, skip = 0, 0

        for i in range(len(nums) - 1):
            take, skip = skip + nums[i], max(take, skip)
        
        take1, skip1 = 0, 0

        for i in range(1, len(nums)):
            take1, skip1 = skip1 + nums[i], max(take1, skip1)
        
        return max(take, skip, take1, skip1)
