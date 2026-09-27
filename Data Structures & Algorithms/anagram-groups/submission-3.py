class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            freq = [0] * 26

            for ch in s:
                freq[ord(ch) - ord("a")] += 1
            
            key = tuple(freq)
            
            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(s)
        
        return list(anagrams.values())
