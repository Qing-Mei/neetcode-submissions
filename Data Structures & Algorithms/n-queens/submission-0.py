class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        queen_cols = [-1] * n

        col = [False] * n
        diag1 = [False] * (2 * n - 1)
        diag2 = [False] * (2 * n - 1)

        def dfs(r):
            if r == n:
                board = []

                for c in queen_cols:
                    board.append("." * c + "Q" + (n - c - 1) * ".")

                res.append(board)
                return

            for c in range(n):
                d1 = r - c + n - 1
                d2 = r + c

                if col[c] or diag1[d1] or diag2[d2]:
                    continue

                queen_cols[r] = c
                col[c] = True
                diag1[d1] = True
                diag2[d2] = True

                dfs(r + 1)

                queen_cols[r] = -1
                col[c] = False
                diag1[d1] = False
                diag2[d2] = False

        dfs(0)
        return res
