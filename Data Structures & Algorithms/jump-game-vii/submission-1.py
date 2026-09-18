class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        dp = [False] * n
        dp[n - 1] = s[n - 1] == "0"

        count = 0

        for i in range(n - 2, -1, -1):
            if i + minJump < n:
                count += dp[i + minJump]
            
            if i + maxJump + 1 < n:
                count -= dp[i + maxJump + 1]
            
            dp[i] = s[i] == "0" and count > 0
        
        return dp[0]
