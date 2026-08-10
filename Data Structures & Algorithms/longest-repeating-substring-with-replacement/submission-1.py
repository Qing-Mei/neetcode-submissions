from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        max_freq = 0
        freq = defaultdict(int)
        l = 0

        for r, ch in enumerate(s):
            freq[ch] += 1
            max_freq = max(max_freq, freq[ch])

            if r - l + 1 - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest
        