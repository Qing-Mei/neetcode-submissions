class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def sift_down(index, heap_size):
            while True:
                largest = index
                left = index * 2 + 1
                right = index * 2 + 2

                if left < heap_size and nums[left] > nums[largest]:
                    largest = left
                
                if right < heap_size and nums[right] > nums[largest]:
                    largest = right
                
                if largest == index:
                    break
                
                nums[index], nums[largest] = nums[largest], nums[index]
                index = largest
        
        # leaf index * 2 + 1
        # n nodes n // 2 - 1
        for i in range(n // 2 - 1, -1, -1):
            sift_down(i, n)
        
        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]

            sift_down(0, end)
        
        return nums
