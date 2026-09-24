class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0

        for i in range(32):
            bit = (left >> i) & 1

            if bit == 0:
                continue
            
            start = left % (1 << (i + 1))
            remain = (1 << (i + 1)) - start

            if right - left < remain:
                res |= (1 << i)
        
        return res
