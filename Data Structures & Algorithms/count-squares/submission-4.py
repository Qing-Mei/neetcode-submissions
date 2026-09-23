from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.pts_count = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        i, j = point
        # (1, 1)
        # {1: {1: 1}}
        self.pts_count[i][j] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point

        col = self.pts_count.get(x1)
        if col is None:
            return 0
        
        for y2, cnt in col.items():
            side = y2 - y1
            if side == 0:
                continue
            
            for x in (x1 + side, x1 - side):
                other = self.pts_count.get(x)

                if other is not None:
                    res += cnt * other.get(y1, 0) * other.get(y2, 0)
        
        return res
