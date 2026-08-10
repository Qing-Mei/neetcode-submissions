class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)

        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num

        def can_divide(maximum):
            cnt = 0
            i = 0

            while i < n:
                target = prefix[i] + maximum

                left, right = i + 1, n + 1

                while left < right:
                    mid = (left + right) // 2

                    if prefix[mid] > target:
                        right = mid
                    else:
                        left = mid + 1
                
                i = left - 1
                cnt += 1

                if cnt > k:
                    return False
            
            return True
        
        l, r = max(nums), sum(nums)

        while l < r:
            m = (l + r) // 2

            if can_divide(m):
                r = m
            else:
                l = m + 1
        
        return l
