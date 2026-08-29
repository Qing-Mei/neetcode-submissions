class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        if not digits:
            return res

        path = []
        letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def dfs(i):
            if i == len(digits):
                res.append("".join(path))
                return
            
            for letter in letters[int(digits[i]) - 2]:
                path.append(letter)
                dfs(i + 1)
                path.pop()
        
        dfs(0)
        return res
