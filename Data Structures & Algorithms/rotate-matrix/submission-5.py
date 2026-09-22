class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        l, r = 0, n - 1

        while l < r:
            for j in range(l, r):
                temp = matrix[l][j]

                matrix[l][j] = matrix[n - 1 - j][l]
                matrix[n - 1 - j][l] = matrix[n - 1 - l][n - 1 - j]
                matrix[n - 1 - l][n - 1 - j] = matrix[j][n - 1 - l]
                matrix[j][n - 1 - l] = temp
            
            l += 1
            r -= 1
        