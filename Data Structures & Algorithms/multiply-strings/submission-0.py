class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                a = ord(num1[i]) - ord("0")
                b = ord(num2[j]) - ord("0")

                total = a * b + res[i + j + 1]

                res[i + j + 1] = total % 10
                res[i + j] += total // 10

        start = 1 if res[0] == 0 else 0

        return "".join(str(digit) for digit in res[start:])
