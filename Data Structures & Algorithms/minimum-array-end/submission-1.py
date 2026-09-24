class Solution:
    def minEnd(self, n: int, x: int) -> int:
        remain = n - 1

        ans = x
        bit = 1

        while remain:
            if (x & bit) == 0:
                if remain & 1:
                    ans |= bit
                
                remain >>= 1
            
            bit <<= 1
        
        return ans
        
