from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = defaultdict(int)
        left = 0
        min_length = len(s) + 1
        start = -1
        valid = 0

        for right, ch in enumerate(s):
            if ch in need:
                window[ch] += 1

                if window[ch] == need[ch]:
                    valid += 1

                    while valid == len(need):
                        if right - left + 1 < min_length:
                            min_length = right - left + 1
                            start = left
                        
                        remove = s[left]
                        if remove in need:
                            if window[remove] == need[remove]:
                                valid -= 1

                            window[remove] -= 1
                        left += 1

        return "" if min_length == len(s) + 1 else s[start:start+min_length]