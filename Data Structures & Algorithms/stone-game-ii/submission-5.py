from functools import cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + piles[i]
        
        @cache
        def dfs(i, limit):
            if i >= n:
                return 0, 0
            
            best, other = 0, 0

            for length in range(1, min(limit, n - i) + 1):
                j = i + length
                mine = prefix[j] - prefix[i]

                other_later, mine_later = dfs(j, max(limit, length * 2))

                if mine + mine_later > best:
                    best = mine + mine_later
                    other = other_later
            
            return best, other
        
        alice, bob = dfs(0, 2)

        return alice

