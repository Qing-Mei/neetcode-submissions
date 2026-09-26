import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(left, right):
            if left >= right:
                return
            
            pivot_index = random.randint(left, right)
            pivot = nums[pivot_index]

            l = left
            i = left
            r = right

            while i <= r:
                if nums[i] < pivot:
                    nums[i], nums[l] = nums[l], nums[i]
                    l += 1
                    i += 1
                
                elif nums[i] > pivot:
                    nums[i], nums[r] = nums[r], nums[i]
                    r -= 1
                
                else:
                    i += 1
            
            quick_sort(left, l - 1)
            quick_sort(r + 1, right)
        
        quick_sort(0, len(nums) - 1)

        return nums
