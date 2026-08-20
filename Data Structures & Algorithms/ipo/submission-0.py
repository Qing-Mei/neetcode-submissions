import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [(cap, profit) for cap, profit in zip(capital, profits)]
        heapq.heapify(projects)

        available = []

        for _ in range(k):
            while projects and projects[0][0] <= w:
                cap, profit = heapq.heappop(projects)
                heapq.heappush(available, (-profit, cap))
            
            if not available:
                break
            
            w += -heapq.heappop(available)[0]
        
        return w
