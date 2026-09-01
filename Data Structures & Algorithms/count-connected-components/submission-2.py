class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n

        def dfs(node):
            visited[node] = True

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)

        cnt = 0

        for node in range(n):
            if not visited[node]:
                dfs(node)
                cnt += 1

        return cnt
