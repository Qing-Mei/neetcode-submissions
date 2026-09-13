from functools import cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dfs(i, j):
            if i > j:
                return 0, 0
            
            other1, mine1 = dfs(i + 1, j)
            other2, mine2 = dfs(i, j - 1)

            if piles[i] + mine1 > piles[j] + mine2:
                mine = piles[i] + mine1
                other = other1
            else:
                mine = piles[j] + mine2
                other = other2

            return mine, other
        
        alice, bob = dfs(0, len(piles) - 1)

        if alice > bob:
            return True
        else:
            return False
