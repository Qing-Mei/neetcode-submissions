class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0
        cnt = 0
        seen = {0: 1}

        for i in range(n):
            prefix += nums[i]
            need = prefix - k

            if need in seen:
                cnt += seen[need]
            
            seen[prefix] = seen.get(prefix, 0) + 1
        
        return cnt
