class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        graph = [[] for _ in range(n)]
        degree = [0] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
        
        leaves = []

        for node in range(n):
            if degree[node] == 1:
                leaves.append(node)
        
        remaining = n

        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                for nei in graph[leaf]:
                    degree[nei] -= 1

                    if degree[nei] == 1:
                        new_leaves.append(nei)
            
            leaves = new_leaves
        
        return leaves
