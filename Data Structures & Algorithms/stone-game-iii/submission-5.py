from functools import cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @cache
        def dfs(i): # curr_player, other_player
            if i == n:
                return 0, 0
            
            best_me = float("-inf")
            best_other = 0
            take = 0

            for j in range(i, min(i + 3, n)):
                take += stoneValue[j]

                other_later, me_later = dfs(j + 1)

                me = take + me_later
                other = other_later

                if me > best_me:
                    best_me = me
                    best_other = other
            
            return best_me, best_other
        
        alice, bob = dfs(0)

        if alice > bob:
            return "Alice"
        if alice < bob:
            return "Bob"
        return "Tie"
