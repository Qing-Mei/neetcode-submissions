import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        for x, y in points:
            res.append((x ** 2 + y ** 2, x, y))
        
        res.sort()

        output = []

        for i in range(k):
            x, y = res[i][1], res[i][2]
            output.append([x, y])

        return output
