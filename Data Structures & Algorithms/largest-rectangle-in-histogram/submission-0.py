class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)

        for i in range(n):
            min_height = heights[i]
            for j in range(i, n):
                min_height = min(min_height, heights[j])
                res = max(res, min_height * (j - i + 1))
        
        return res
