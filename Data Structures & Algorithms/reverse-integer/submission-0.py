class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        n = abs(x)

        while n:
            res = res * 10 + n % 10
            n //= 10
        
        if x < 0:
            res = -res
        
        return res if -2 ** 31 <= res <= 2 ** 31 - 1 else 0
