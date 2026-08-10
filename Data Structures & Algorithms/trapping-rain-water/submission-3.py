class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        stack = []

        for r, r_height in enumerate(height):
            while stack and height[stack[-1]] < r_height:
                bottom = height[stack.pop()]
            
                if stack:
                    l = stack[-1]
                    l_height = height[l]
                    water += (min(l_height, r_height) - bottom) * (r - l - 1)

            stack.append(r)
        
        return water
