from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))
        
        def dfs(node, target, product, visited):
            if node == target:
                return product
            
            for nxt, val in graph[node]:
                if nxt in visited:
                    continue

                visited.add(nxt)

                res = dfs(nxt, target, product * val, visited)
            
                if res != -1:
                    return res

            return -1

        res = []

        for a, b in queries:
            if a not in graph or b not in graph:
                res.append(-1)
                continue

            visited = {a}
            res.append(dfs(a, b, 1.0, visited))
        
        return res
