class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[course].append(pre)
        
        state = [0] * numCourses
        res = []
        def dfs(node):
            if state[node] == 1:
                return False
            
            if state[node] == 2:
                return True
            
            state[node] = 1

            for pre in graph[node]:
                if dfs(pre) == False:
                    return False
            
            state[node] = 2
            res.append(node)
            
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        
        return res
