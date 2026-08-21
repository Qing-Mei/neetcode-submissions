import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        time = 0
        available = []
        
        remain = [(start, process, i) for i, (start, process) in enumerate(tasks)]
        remain.sort()

        res = []
        j = 0

        while len(res) < n:
            if not available and j < n and remain[j][0] > time:
                time = remain[j][0]
            
            while j < n and remain[j][0] <= time:
                start, process, i = remain[j]
                heapq.heappush(available, (process, i))
                j += 1
            
            process, i = heapq.heappop(available)
            res.append(i)
            time += process

        return res
        