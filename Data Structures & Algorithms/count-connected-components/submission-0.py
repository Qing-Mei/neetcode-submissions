from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node):
            visited.add(node)

            for nxt in graph[node]:
                if nxt not in visited:
                    dfs(nxt)
        
        visited = set()

        cnt = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                cnt += 1
        
        return cnt
        