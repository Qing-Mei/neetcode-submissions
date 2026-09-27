class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0] * 9
        col = [0] * 9
        box = [0] * 9

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                
                num = int(board[i][j])
                box_idx = (i // 3) * 3 + (j // 3)

                if row[i] & (1 << num) or col[j] & (1 << num) or box[box_idx] & (1 << num):
                    return False
                
                row[i] |= (1 << num)
                col[j] |= (1 << num)
                box[box_idx] |= (1 << num)
            
        return True
