class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def get_height(node, visited):
            h = -1
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    h = max(h, get_height(child, visited))

            return h + 1
        
        min_height = n + 1
        roots = []
        for node in range(n):
            visited = {node}
            h = get_height(node, visited)

            if h < min_height:
                min_height = h
                roots = [node]

            elif h == min_height:
                roots.append(node)
        
        return roots
