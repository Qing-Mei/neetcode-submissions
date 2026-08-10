class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_divide(maximum):
            curr = 0
            cnt = 1

            for num in nums:
                if curr + num > maximum:
                    curr = num
                    cnt += 1
                else:
                    curr += num
            
            return cnt <= k
        
        l, r = max(nums), sum(nums)

        while l < r:
            m = (l + r) // 2

            if can_divide(m):
                r = m
            else:
                l = m + 1
        
        return l
