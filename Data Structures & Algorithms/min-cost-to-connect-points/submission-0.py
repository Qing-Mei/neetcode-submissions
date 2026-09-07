class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        min_dist = [float("inf")] * n
        min_dist[0] = 0

        visited = [False] * n
        total_cost = 0

        for _ in range(n):
            curr = -1

            for i in range(n):
                if not visited[i] and (curr == -1 or min_dist[i] < min_dist[curr]):
                    curr = i
            
            visited[curr] = True
            total_cost += min_dist[curr]

            x1, y1 = points[curr]

            for nei in range(n):
                if not visited[nei]:
                    x2, y2 = points[nei]
                    distance = abs(x1 - x2) + abs(y1 - y2)

                    min_dist[nei] = min(min_dist[nei], distance)
        
        return total_cost
