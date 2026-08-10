class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def get_length(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            
            return i + 1, j - 1

        start, end = 0, 0

        for i in range(len(s)):
            s1, e1 = get_length(i, i)
            if e1 - s1 > end - start:
                start, end = s1, e1

            s2, e2 = get_length(i, i + 1)
            if e2 - s2 > end - start:
                start, end = s2, e2
        
        return s[start:end + 1]
