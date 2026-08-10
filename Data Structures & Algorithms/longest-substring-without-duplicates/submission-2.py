class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        res = 0

        for r, ch in enumerate(s):
            if ch in seen:
                l = max(l, seen[ch] + 1)
            res = max(res, r - l + 1)
            seen[ch] = r
        
        return res
