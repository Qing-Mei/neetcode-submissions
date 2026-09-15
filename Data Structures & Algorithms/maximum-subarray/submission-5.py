class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def solve(left, right): # return total, prefix, suffix, best in range(left, right + 1)
            if left == right:
                x = nums[left]
                return x, x, x, x
            
            mid = (left + right) // 2

            l_total, l_prefix, l_suffix, l_best = solve(left, mid)
            r_total, r_prefix, r_suffix, r_best = solve(mid + 1, right)

            total = l_total + r_total

            prefix = max(l_prefix, l_total + r_prefix)

            suffix = max(r_suffix, r_total + l_suffix)

            best = max(l_best, r_best, l_suffix + r_prefix)

            return total, prefix, suffix, best
        
        return solve(0, len(nums) - 1)[3]
