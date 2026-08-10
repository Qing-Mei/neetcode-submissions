import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(left, right):
            if left >= right:
                return
            
            pivot_index = random.randint(left, right)
            pivot = nums[pivot_index]

            # [0  lt] < pivot
            # [gt  n] > pivot
            # [lt  i] = pivot
            # [i  gt] uncheck
            lt = left
            i = left
            gt = right

            while i <= gt:
                if nums[i] < pivot:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    lt += 1
                    i += 1
                
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1

                else:
                    i += 1
            
            quick_sort(left, lt - 1)
            quick_sort(gt + 1, right)
        
        quick_sort(0, len(nums) - 1)

        return nums
        