class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        res = []
        i, j = 0, -1
        top, bottom, left, right = 0, m - 1, 0, n - 1

        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                res.append(matrix[i][j])
            top += 1

            for i in range(top, bottom + 1):
                res.append(matrix[i][j])
            right -= 1

            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[i][j])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][j])
                left += 1

        return res
