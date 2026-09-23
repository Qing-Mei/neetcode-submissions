class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        i, j = point
        self.points[(i, j)] = self.points.get((i, j), 0) + 1

    def count(self, point: List[int]) -> int:
        i, j = point
        res = 0

        for (x, y), freq in self.points.items():
            if x == i or abs(x - i) != abs(y - j):
                continue
            
            res += freq * self.points.get((i, y), 0) * self.points.get((x, j), 0)

        return res
        