class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = [0] * 26
        window = [0] * 26
        k = len(s1)
        cnt = 0

        for ch in s1:
            need[ord(ch) - ord("a")] += 1
        
        target = sum(freq > 0 for freq in need)

        def update(index, delta):
            nonlocal cnt

            if need[index] > 0 and window[index] == need[index]:
                cnt -= 1
            
            window[index] += delta

            if need[index] > 0 and window[index] == need[index]:
                cnt += 1
        
        for r, ch in enumerate(s2):
            update(ord(ch) - ord("a"), 1)

            if r >= k:
                update(ord(s2[r - k]) - ord("a"), -1)

            if r >= k - 1 and cnt == target:
                return True
            
        return False
