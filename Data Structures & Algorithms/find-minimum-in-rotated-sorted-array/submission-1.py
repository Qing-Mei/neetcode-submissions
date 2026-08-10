class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1. sorted array normal   nums[l]  <  nums[m]   < nums[r]
        # 2. left side bigger than right side     
        #      nums[m] > nums[r] 
        #      nums[m] <= nums[r]

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        return nums[l]
        