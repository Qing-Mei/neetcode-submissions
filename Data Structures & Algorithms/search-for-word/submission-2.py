class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        m = len(board)
        n = len(board[0])

        def dfs(i, j, index):    
            if board[i][j] != word[index]:
                return False

            if index == len(word) - 1:
                return True
            
            board[i][j] = "#"

            for di, dj in dirs:
                ni = i + di
                nj = j + dj

                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != "#" and dfs(ni, nj, index + 1):
                    board[i][j] = word[index]
                    return True
            
            board[i][j] = word[index]
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False
