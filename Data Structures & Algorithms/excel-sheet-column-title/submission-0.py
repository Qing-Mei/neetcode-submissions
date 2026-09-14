class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber:
            columnNumber -= 1
            digit = columnNumber % 26
            res.append(chr(ord("A") + digit))
            columnNumber //= 26

        return "".join(reversed(res))
