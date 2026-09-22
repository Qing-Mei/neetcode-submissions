class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        
        if n == 0:
            return 1
        
        res = 1
        base = x

        while n:
            if n & 1:
                res *= base

            base *= base
            n >>= 1
        
        return res
