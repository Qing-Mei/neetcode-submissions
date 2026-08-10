class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r + 1) // 2

            if nums[m] <= nums[r]:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m
            else:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m
        
        return l if nums[l] == target else -1
