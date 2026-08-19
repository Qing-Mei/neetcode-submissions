import heapq
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldown = deque()
        time = 0

        counter = Counter(tasks)
        available = [-freq for freq in counter.values()]
        heapq.heapify(available)

        while available or cooldown:
            time += 1

            if available:
                freq = heapq.heappop(available)

                freq += 1

                if freq != 0:
                    cooldown.append((freq, time + n))
            
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(available, cooldown.popleft()[0])
                    
        return time
