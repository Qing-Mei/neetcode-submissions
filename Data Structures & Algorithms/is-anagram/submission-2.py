class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cnt = [0] * 26
        for i in range(len(s)):
            ch_s, ch_t = s[i], t[i]

            cnt[ord(ch_s) - ord('a')] += 1
            cnt[ord(ch_t) - ord('a')] -= 1
        
        return all(x == 0 for x in cnt)
        