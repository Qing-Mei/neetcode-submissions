class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        n = len(s)
        
        dp = [[False] * n for _ in range(n)]
        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                if s[left] == s[right]:
                    if length <= 2 or dp[left + 1][right - 1]:
                        dp[left][right] = True

        def dfs(start):
            if start == n:
                res.append(path[:])
                return
            
            for end in range(start, n):
                if not dp[start][end]:
                    continue
                
                path.append(s[start:end+1])
                dfs(end + 1)
                path.pop()
        
        dfs(0)
        return res
