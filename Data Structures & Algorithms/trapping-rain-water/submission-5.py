class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = height[0]
        right_max = height[-1]
        total = 0
        l = 0
        r = n - 1
        
        while l < r:
            if left_max < right_max:
                h = height[l + 1]
                if h < left_max:
                    total += left_max - h
                else:
                    left_max = h
                l += 1
            else:
                h = height[r - 1]
                if h < right_max:
                    total += right_max - h
                else:
                    right_max = h
                r -= 1
        
        return total
