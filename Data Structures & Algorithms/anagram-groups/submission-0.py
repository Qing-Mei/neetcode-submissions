from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for s in strs:
            s1 = "".join(sorted(s))

            seen[s1].append(s)

        return list(seen.values())
