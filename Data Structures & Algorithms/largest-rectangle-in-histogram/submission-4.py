class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] > heights[i]):
                prev_height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, prev_height * width)
            stack.append(i)
        
        return max_area
