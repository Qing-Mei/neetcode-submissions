class Solution:
    def countSubstrings(self, s: str) -> int:
        def count(i, j):
            cnt = 0

            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
                cnt += 1
            
            return cnt
        
        n = len(s)
        res = 0

        for i in range(n):
            res += count(i, i)
            res += count(i, i + 1)
        
        return res
        