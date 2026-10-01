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
            while (curr + k) % n != start:
                nxt = (curr + k) % n
                nums[start], nums[nxt] = nums[nxt], nums[start]
                curr = nxt
            
        