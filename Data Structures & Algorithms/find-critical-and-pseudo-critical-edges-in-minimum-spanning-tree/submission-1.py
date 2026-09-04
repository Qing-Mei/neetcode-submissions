class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        sorted_edges = []

        for index, (a, b, weight) in enumerate(edges):
            sorted_edges.append((weight, a, b, index))
        
        sorted_edges.sort()

        def kruskal(skip=-1, force=-1):
            parent = list(range(n))
            size = [1] * n

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]
            
            def union(x, y):
                root_x = find(x)
                root_y = find(y)

                if root_x == root_y:
                    return False
                
                if size[root_x] < size[root_y]:
                    root_x, root_y = root_y, root_x
                
                parent[root_y] = root_x
                size[root_x] += size[root_y]

                return True
            
            total_weight = 0
            edge_count = 0

            if force != -1:
                weight, a, b, _ = sorted_edges[force]

                if union(a, b):
                    total_weight += weight
                    edge_count += 1
            
            for i, (weight, a, b, _) in enumerate(sorted_edges):
                if i == skip or i == force:
                    continue
                
                if union(a, b):
                    total_weight += weight
                    edge_count += 1
                    
                    if edge_count == n - 1:
                        break
                
            if edge_count != n - 1:
                return float("inf")
            
            return total_weight
        
        normal_weight = kruskal()

        critical = []
        pseudo_critical = []

        for i, (_, _, _, original_index) in enumerate(sorted_edges):
            if kruskal(skip=i) > normal_weight:
                critical.append(original_index)
            elif kruskal(force=i) == normal_weight:
                pseudo_critical.append(original_index)
        
        return [critical, pseudo_critical]
