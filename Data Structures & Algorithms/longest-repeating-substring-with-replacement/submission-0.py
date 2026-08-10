class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        max_count = 0
        ans = 0

        for r, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            max_count = max(max_count, count[ch])

            while (r - l + 1) - max_count > k:
                count[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans
        