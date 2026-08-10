class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0] * 9
        col = [0] * 9
        box = [0] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                curr = 1 << (int(board[i][j]) - 1)
                idx = (i // 3) * 3 + (j // 3)

                if row[i] & curr or col[j] & curr or box[idx] & curr:
                    return False

                row[i] |= curr
                col[j] |= curr
                box[idx] |= curr
        
        return True
