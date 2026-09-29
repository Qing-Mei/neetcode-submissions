class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        left = [0] * n
        right = [0] * n

        for i in range(n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
        
        for i in range(n - 1, -1, -1):
            if i == n - 1 or (i + 1) % k == 0:
                right[i] = nums[i]
            else:
                right[i] = max(right[i + 1], nums[i])
        
        res = []

        for l in range(n - k + 1):
            r = l + k - 1
            res.append(max(right[l], left[r]))

        return res
        