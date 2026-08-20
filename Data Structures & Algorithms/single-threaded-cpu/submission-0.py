import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)

        remain = [(start, process, i) for i, (start, process) in enumerate(tasks)]
        remain.sort()

        available = []
        res = []

        time = 0
        j = 0

        while len(res) < n:
            if not available and j < n and time < remain[j][0]:
                time = remain[j][0]

            while j < n and remain[j][0] <= time:
                start, process, i = remain[j]
                heapq.heappush(available, (process, i))
                j += 1
            
            process, i = heapq.heappop(available)
            res.append(i)
            time += process

        return res
