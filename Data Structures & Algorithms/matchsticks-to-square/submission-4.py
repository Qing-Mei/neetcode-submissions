class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        total = sum(matchsticks)

        if n < 4 or total % 4 != 0:
            return False
        
        target = total // 4

        if max(matchsticks) > target:
            return False
        
        # dp[000000] dp[000001] dp[000010] dp[000011] .. dp[111111]
        dp = [-1] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] == -1:
                continue
            
            for i in range(n):
                if mask & (1 << i):
                    continue
                
                new_length = dp[mask] + matchsticks[i]

                if new_length > target:
                    continue
                
                next_mask = mask | (1 << i)
                dp[next_mask] = new_length % target
        
        return dp[(1 << n) - 1] == 0
