from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        def dfs(node):
            visited.add(node)

            for nxt in graph[node]:
                if nxt not in visited:
                    dfs(nxt)
        
        dfs(0)

        return len(visited) == n
        