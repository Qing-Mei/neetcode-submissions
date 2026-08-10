class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                curr = num

                while curr in nums_set:
                    curr += 1
                
                longest = max(longest, curr - num)
        
        return longest
