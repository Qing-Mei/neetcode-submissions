from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)

        if max(counter.values()) > (len(s) + 1) // 2:
            return ""

        max_heap = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(max_heap)

        res = []
        prev_count = 0
        prev_char = ""

        while max_heap:
            cnt, char = heapq.heappop(max_heap)

            res.append(char)
            cnt += 1

            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            
            prev_count = cnt
            prev_char = char

        return "".join(res)
