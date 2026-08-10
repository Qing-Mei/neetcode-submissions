class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = (1 << 32) - 1
        max_int = (1 << 31) - 1

        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        return a if a <= max_int else a - (1 << 32)
