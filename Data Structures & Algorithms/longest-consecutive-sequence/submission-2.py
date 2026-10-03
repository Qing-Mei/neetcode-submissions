class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        res = 0

        for num in seen:
            if num - 1 not in seen:
                curr = num
                length = 1

                while curr + 1 in seen:
                    curr += 1
                    length += 1
                
                res = max(res, length)
            
        return res

