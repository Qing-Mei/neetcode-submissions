import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, time in times:
            graph[u].append((v, time))
        
        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        min_heap = [(0, k)]

        while min_heap:
            curr_time, node = heapq.heappop(min_heap)

            if curr_time > dist[node]:
                continue
            
            for nei, travel_time in graph[node]:
                new_time = curr_time + travel_time

                if new_time < dist[nei]:
                    dist[nei] = new_time

                    heapq.heappush(min_heap, (new_time, nei))
        
        ans = max(dist[1:])

        return ans if ans < float("inf") else -1
