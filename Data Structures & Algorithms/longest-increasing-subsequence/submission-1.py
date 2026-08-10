import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        arr = []

        for i in range(n):
            idx = bisect.bisect_left(arr, nums[i])

            if idx == len(arr):
                arr.append(nums[i])
            else:
                arr[idx] = nums[i]

        return len(arr)
