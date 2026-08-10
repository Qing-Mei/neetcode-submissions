class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0

        for num in num_set:
            if num - 1 not in num_set:
                cur = num
                length = 1

                while cur + 1 in num_set:
                    cur += 1
                    length += 1
                
                ans = max(ans, length)
        
        return ans
        