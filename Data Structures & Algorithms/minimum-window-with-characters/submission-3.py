from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need = Counter(t)
        window = defaultdict(int)

        min_length = len(s) + 1
        min_start = -1
        valid = 0
        l = 0

        for r, ch in enumerate(s):
            if ch in need:
                window[ch] += 1

                if window[ch] == need[ch]:
                    valid += 1

                    while valid == len(need):
                        if r - l + 1 < min_length:
                            min_length = r - l + 1
                            min_start = l

                        if s[l] in need:
                            if window[s[l]] == need[s[l]]:
                                valid -= 1

                        window[s[l]] -= 1
                        l += 1
        
        return s[min_start:min_start+min_length] if min_start != -1 else ""
