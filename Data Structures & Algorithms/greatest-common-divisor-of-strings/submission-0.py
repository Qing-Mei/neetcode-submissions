class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        for length in range(min(m, n), 0, -1):
            if m % length != 0 or n % length != 0:
                continue
            
            x = str1[:length]

            if x * (m // length) == str1 and x * (n // length) == str2:
                return x
        
        return ""
        