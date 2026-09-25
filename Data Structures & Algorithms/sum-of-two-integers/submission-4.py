class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        a &= MASK
        b &= MASK

        while a:
            carry = ((a & b) << 1) & MASK
            b = a ^ b
            a = carry
        
        return b if b <= MAX_INT else ~(b ^ MASK)
