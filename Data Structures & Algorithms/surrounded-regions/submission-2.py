from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        m = len(board)
        n = len(board[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == "O":
                    q.append((i, j))
        
        while q:
            x, y = q.popleft()

            board[x][y] = "T"
        
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == "O":
                    q.append((nx, ny))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"

