from collections import deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo(edges):
            graph = [[] for _ in range(k + 1)]
            indegree = [0] * (k + 1)

            for a, b in edges:
                graph[a].append(b)
                indegree[b] += 1
            
            order = []
            q = deque()

            for i in range(1, k + 1):
                if indegree[i] == 0:
                    q.append(i)
            
            while q:
                node = q.popleft()
                order.append(node)

                for nxt in graph[node]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        q.append(nxt)
            
            return order
        
        row_order = topo(rowConditions)
        if len(row_order) != k:
            return []

        col_order = topo(colConditions)
        if len(col_order) != k:
            return []
        
        res = [[0] * k for _ in range(k)]

        num_to_col = [0] * (k + 1)
        for col, num in enumerate(col_order):
            num_to_col[num] = col
        
        for row, num in enumerate(row_order):
            col = num_to_col[num]
            res[row][col] = num
        
        return res
