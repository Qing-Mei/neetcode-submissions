class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        if n == 0:
            return

        k %= n

        if k == 0:
            return

        cycles = math.gcd(n, k)

        for start in range(cycles):
            curr = start

            while True:
                nxt = (curr + k) % n

                nums[start], nums[nxt] = nums[nxt], nums[start]

                curr = nxt

                if curr == start:
                    break

