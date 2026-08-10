class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        ans = 0
        l = 0

        for r in range(len(s)):
            if s[r] in seen:
                l = max(l, seen[s[r]] + 1)
            
            ans = max(ans, r - l + 1)
            seen[s[r]] = r
        
        return ans
