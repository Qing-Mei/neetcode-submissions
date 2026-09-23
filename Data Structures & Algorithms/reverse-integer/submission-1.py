class Solution:
    def reverse(self, x: int) -> int:
        res = 0

        MAX = 2 ** 31 - 1
        MIN = -2 ** 31

        while x:
            if x < 0:
                digit = x % 10
                if digit != 0:
                    digit -= 10
            else:
                digit = x % 10
            
            x = (x - digit) // 10

            if res > MAX // 10 or (res == MAX // 10 and digit > 7):
                return 0
            
            if res < (MIN // 10 + 1) or (res == (MIN // 10 + 1) and digit < -8):
                return 0

            res = res * 10 + digit
        
        return res
