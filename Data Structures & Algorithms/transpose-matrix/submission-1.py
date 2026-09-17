class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        if m == n:
            for i in range(m):
                for j in range(i + 1, m):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            return matrix

        res = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                res[j][i] = matrix[i][j]
        
        return res
