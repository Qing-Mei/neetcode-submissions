class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        m = len(board)
        n = len(board[0])

        def dfs(board, word, i, j, idx):
            if idx == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[idx]:
                return False
            
            char = board[i][j]
            board[i][j] = "#"

            for di, dj in dirs:
                ni = i + di
                nj = j + dj

                if dfs(board, word, ni, nj, idx + 1):
                    board[i][j] = char
                    return True
            
            board[i][j] = char
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(board, word, i, j, 0):
                    return True
        
        return False
