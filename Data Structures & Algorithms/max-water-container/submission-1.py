class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer pushing from both sides, each time width = r - l, height = min(heights[l], heights[r])
        # each moving from the lower side

        l, r = 0, len(heights) - 1

        ans = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])

            ans = max(ans, width * height)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return ans
        