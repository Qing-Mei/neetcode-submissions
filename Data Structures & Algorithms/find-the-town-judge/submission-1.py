from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        diff = defaultdict(int)

        for a, b in trust:
            diff[a] -= 1
            diff[b] += 1
        
        for i in range(1, n + 1):
            if diff[i] == n - 1:
                return i
        
        return -1
