class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "@" + "#" + "#".join(s) + "#" + "$"
        n = len(t)
        p = [0] * n
        center, right = 0, 0
        max_len = -1
        start = -1

        for i in range(1, n - 1):
            if i < right:
                mirror = 2 * center - i
                p[i] = min(right - i, p[mirror])
            
            while t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1
            
            if i + p[i] > right:
                center, right = i, i + p[i]
            
            if p[i] > max_len:
                max_len = p[i]
                start = (i - max_len) // 2
        
        return s[start:start + max_len]
