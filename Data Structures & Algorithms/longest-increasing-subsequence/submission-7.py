import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []

        for i in range(len(nums)):
            idx = bisect.bisect_left(tail, nums[i])

            if idx == len(tail):
                tail.append(nums[i])
            else:
                tail[idx] = nums[i]
        
        return len(tail)
        