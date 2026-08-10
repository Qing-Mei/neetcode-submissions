class Solution:
    def getSum(self, a: int, b: int) -> int:
        # (a & b) << 1 carry
        # a ^ b sum without carry
        mask = (1 << 32) - 1
        max_int = (1 << 31) - 1

        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        # 01111111 11111111 11111111 11111111
        # 11111111 11111111 11111111 11111111

        return a if a <= max_int else a - (1 << 32)
