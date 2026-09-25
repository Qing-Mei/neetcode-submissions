import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = [-1] * len(queries)

        heap = [] # [interval length, end of interval]
        i = 0

        for time, idx in sorted((time, idx) for idx, time in enumerate(queries)):
            while i < len(intervals) and intervals[i][0] <= time:
                start, end = intervals[i]
                heapq.heappush(heap, (end - start + 1, end))
                i += 1

            while heap and heap[0][1] < time:
                heapq.heappop(heap)
            
            if heap:
                res[idx] = heap[0][0]
        
        return res
