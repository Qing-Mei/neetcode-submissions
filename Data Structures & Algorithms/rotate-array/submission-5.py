import math

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        if k == 0:
            return

        for start in range(math.gcd(n, k)):
            curr = start
            carried = nums[start]
            
            while True:
                nxt = (curr + k) % n
                carried, nums[nxt] = nums[nxt], carried
                curr = nxt

                if curr == start:
                    break
            
        