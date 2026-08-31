class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        m = len(board)
        n = len(board[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            board[x][y] = "T"

            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == "O":
                    dfs(nx, ny)

        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n - 1] == "O":
                dfs(i, n - 1)
        
        for j in range(n):
            if board[0][j] == "O":
                dfs(0, j)
            if board[m - 1][j] == "O":
                dfs(m - 1, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
