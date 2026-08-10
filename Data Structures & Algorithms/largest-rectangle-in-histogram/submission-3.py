class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                index, prev_height = stack.pop()
                width = i - index
                max_area = max(max_area, prev_height * width)
                start = index
            
            stack.append((start, height))

        n = len(heights)

        while stack:
            index, height = stack.pop()
            max_area = max(max_area, height * (n - index))
        
        return max_area
        
