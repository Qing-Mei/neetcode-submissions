class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        n = len(s)

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(start):
            if start == n:
                res.append(path[:])
                return
            
            for end in range(start, n):
                if not is_palindrome(start, end):
                    continue
                
                path.append(s[start:end+1])
                dfs(end + 1)
                path.pop()
        
        dfs(0)
        return res
