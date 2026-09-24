class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        res = [0] * (max(m, n) + 1)

        i, j = m - 1, n - 1
        k = len(res) - 1
        carry = 0

        while i >= 0 or j >= 0 or carry:
            num1 = int(a[i]) if i >= 0 else 0
            num2 = int(b[j]) if j >= 0 else 0

            total = num1 + num2 + carry
            res[k] = str(total % 2)
            carry = total // 2

            k -= 1
            i -= 1
            j -= 1
        
        return "".join(res[k + 1:])
