from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        res = []
        while q:
            course = q.popleft()
            res.append(course)

            for nxt in graph[course]:
                indegree[nxt] -= 1

                if indegree[nxt] == 0:
                    q.append(nxt)
        
        return res if len(res) == numCourses else []
