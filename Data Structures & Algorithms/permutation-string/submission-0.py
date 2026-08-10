class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)

        if window_size > len(s2):
            return False
        
        counts = [0] * 26

        for ch in s1:
            counts[ord(ch) - ord("a")] += 1
        
        for i, ch in enumerate(s2):
            counts[ord(ch) - ord("a")] -= 1

            if i >= window_size:
                remove = s2[i - window_size]
                counts[ord(remove) - ord("a")] += 1
            
            if i >= window_size - 1 and all(x == 0 for x in counts):
                return True
        
        return False
        