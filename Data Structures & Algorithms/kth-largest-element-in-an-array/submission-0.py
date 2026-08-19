import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k

        def quickselect(left, right):
            if left >= right:
                return nums[left]
            
            pivot = nums[random.randint(left, right)]
            l = left
            g = right
            i = left

            while i <= g:
                if nums[i] < pivot:
                    nums[i], nums[l] = nums[l], nums[i]
                    l += 1
                    i += 1

                elif nums[i] > pivot:
                    nums[i], nums[g] = nums[g], nums[i]
                    g -= 1

                else:
                    i += 1
            
            if target < l:
                return quickselect(left, l - 1)
            elif target > g:
                return quickselect(g + 1, right)
            else:
                return pivot

        return quickselect(0, len(nums) - 1)
