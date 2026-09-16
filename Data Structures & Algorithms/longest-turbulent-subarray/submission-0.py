class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        max_size = 1
        prev = 0

        for r in range(1, len(arr)):
            curr = (arr[r] > arr[r - 1]) - (arr[r] < arr[r - 1])

            if curr == 0:
                l = r
            elif curr == prev:
                l = r - 1
            
            max_size = max(max_size, r - l + 1)
            prev = curr
        
        return max_size
