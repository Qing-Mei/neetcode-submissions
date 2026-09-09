from functools import cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        n = len(stoneValue)
        @cache
        def dfs(i):
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
        
        '''
        n = len(stoneValue)

        def dfs(i):
            if i == n:
                return 0
            
            best = float("-inf")
            take = 0

            for j in range(i, min(i + 3, n)):
                take += stoneValue[j]
                best = max(best, take - dfs(j + 1))
            
            return best
        
        res = dfs(0)

        if res > 0:
            return "Alice"
        if res < 0:
            return "Bob"
        return "Tie"
        '''
        '''
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = float("-inf")
            take = 0

            for j in range(i, min(i + 3, n)):
                take += stoneValue[j]

                dp[i] = max(dp[i], take - dp[j + 1])
        
        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"
        '''
