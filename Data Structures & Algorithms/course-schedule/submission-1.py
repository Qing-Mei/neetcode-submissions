from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, precourse in prerequisites:
            graph[precourse].append(course)
            indegree[course] += 1
        
        q = deque()
        finished = 0

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        while q:
            precourse = q.popleft()
            finished += 1

            for course in graph[precourse]:
                indegree[course] -= 1

                if indegree[course] == 0:
                    q.append(course)

        return finished == numCourses
