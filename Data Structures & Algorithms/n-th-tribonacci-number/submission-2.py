class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n

        def multiply(a, b):
            c = [[0] * 3 for _ in range(3)]

            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        c[i][j] += a[i][k] * b[k][j]
            
            return c
        
        base = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]

        res = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

        power = n - 2

        while power:
            if power % 2 == 1:
                res = multiply(res, base)
            
            base = multiply(base, base)
            power //= 2
        
        return res[2][1] + res[2][2]

        
