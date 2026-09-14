class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return ""

        n = columnNumber - 1

        return self.convertToTitle(n // 26) + chr(ord("A") + n % 26)
