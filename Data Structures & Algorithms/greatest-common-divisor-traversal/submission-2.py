class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)

        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if math.gcd(nums[i], nums[j]) > 1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visited = [False] * n
        def dfs(node):
            visited[node] = True

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)
        
        dfs(0)

        for node in visited:
            if node is False:
                return False
        
        return True
