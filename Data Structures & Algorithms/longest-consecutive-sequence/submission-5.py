class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = {}

        res = 0

        for num in nums:
            if num not in length:
                length[num] = length.get(num - 1, 0) + length.get(num + 1, 0) + 1
                length[num - length.get(num - 1, 0)] = length[num]
                length[num + length.get(num + 1, 0)] = length[num]
                res = max(res, length[num])
 
        return res
