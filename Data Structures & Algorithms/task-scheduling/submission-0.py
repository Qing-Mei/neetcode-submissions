import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_freq = [-freq for freq in count.values()]
        heapq.heapify(max_freq)

        cooldown = deque()
        time = 0

        while max_freq or cooldown:
            time += 1

            if max_freq:
                freq = heapq.heappop(max_freq)
                freq += 1

                if freq != 0:
                    cooldown.append((freq, time + n))
                
            if cooldown and cooldown[0][1] == time:
                freq, _ = cooldown.popleft()
                heapq.heappush(max_freq, freq)
        
        return time
