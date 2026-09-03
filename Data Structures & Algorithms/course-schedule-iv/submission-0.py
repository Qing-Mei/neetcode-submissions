class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)
        
        sources = [pre for pre, _ in queries]
        reachable = {}

        def dfs(node, visited):
            for next_course in graph[node]:
                if next_course not in visited:
                    visited.add(next_course)
                    dfs(next_course, visited)
        
        for source in sources:
            visited = set()
            dfs(source, visited)
            reachable[source] = visited
        
        return [course in reachable[pre] for pre, course in queries]
