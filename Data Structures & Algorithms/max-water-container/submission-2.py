class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        most_water = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            most_water = max(most_water, height * width)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return most_water
