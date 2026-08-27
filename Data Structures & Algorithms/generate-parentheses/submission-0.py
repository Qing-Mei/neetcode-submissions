class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(l, r):
            if l == n and r == n:
                res.append("".join(path))
                return
            
            if l < n:
                path.append("(")
                dfs(l + 1, r)
                path.pop()
            
            if r < l:
                path.append(")")
                dfs(l, r + 1)
                path.pop()
        
        dfs(0, 0)
        return res
