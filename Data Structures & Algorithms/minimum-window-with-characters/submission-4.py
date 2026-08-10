from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need = Counter(t)
        window = defaultdict(int)

        have = 0
        l = 0

        start = -1
        length = len(s) + 1

        for r in range(len(s)):
            if s[r] in need:
                window[s[r]] += 1

                if window[s[r]] == need[s[r]]:
                    have += 1

                    while have == len(need):
                        if r - l + 1 < length:
                            length = r - l + 1
                            start = l

                        if s[l] in need:
                            if window[s[l]] == need[s[l]]:
                                have -= 1
                        
                        window[s[l]] -= 1
                        l += 1
        
        return "" if start == -1 else s[start:start+length]
