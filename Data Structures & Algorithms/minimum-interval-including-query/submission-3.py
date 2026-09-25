import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        START, QUERY, END = 0, 1, 2
        events= []

        for idx, (start, end) in enumerate(intervals):
            events.append((start, START, idx))
            events.append((end, END, idx))
        
        for idx, q in enumerate(queries):
            events.append((q, QUERY, idx))
        
        events.sort()

        heap = []
        inactive = [False] * len(intervals)
        res = [-1] * len(queries)

        for time, event_type, idx in events:
            if event_type == START:
                start, end = intervals[idx]
                heapq.heappush(heap, (end - start + 1, idx))
            
            elif event_type == END:
                inactive[idx] = True
            
            else:
                while heap and inactive[heap[0][1]]:
                    heapq.heappop(heap)
                
                if heap:
                    res[idx] = heap[0][0]
        
        return res
