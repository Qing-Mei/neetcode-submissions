class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = right

        while res > left:
            res &= res - 1
        
        return res
        