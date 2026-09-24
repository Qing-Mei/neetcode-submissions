class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []

        top, down, left, right = 0, m - 1, 0, n - 1

        while top <= down and left <= right:
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            
            top += 1

            for i in range(top, down + 1):
                res.append(matrix[i][right])
            
            right -= 1

            if top <= down:
                for j in range(right, left - 1, - 1):
                    res.append(matrix[down][j])

            down -= 1

            if left <= right:
                for i in range(down, top - 1, -1):
                    res.append(matrix[i][left])
            
            left += 1

        return res
        