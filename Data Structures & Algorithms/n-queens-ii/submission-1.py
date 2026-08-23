class Solution:
    def totalNQueens(self, n: int) -> int:
        cnt = 0

        col = 0
        diag1 = 0
        diag2 = 0

        def dfs(r):
            nonlocal col, diag1, diag2, cnt

            if r == n:
                cnt += 1
                return
            
            for c in range(n):
                d1 = r - c + n - 1
                d2 = r + c
                
                if ((1 << c) & col) or ((1 << d1) & diag1) or ((1 << d2) & diag2):
                    continue
                
                col |= (1 << c)
                diag1 |= (1 << d1)
                diag2 |= (1 << d2)
                dfs(r + 1)

                col ^= (1 << c)
                diag1 ^= (1 << d1)
                diag2 ^= (1 << d2)

        dfs(0)

        return cnt
