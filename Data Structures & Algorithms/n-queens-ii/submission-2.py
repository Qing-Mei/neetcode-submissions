class Solution:
    def totalNQueens(self, n: int) -> int:
        mask = (1 << n) - 1

        def dfs(col, diag1, diag2):
            if col == mask:
                return 1

            available = mask & ~(col | diag1 | diag2)
            cnt = 0

            while available:
                bit = available & -available
                available ^= bit

                cnt += dfs(col | bit, ((diag1 | bit) << 1) & mask, ((diag2 | bit) >> 1))
            
            return cnt

        return dfs(0, 0, 0)
