from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        max_heap = [(-freq, char) for char, freq in Counter(s).items()]
        heapq.heapify(max_heap)

        res = []
        prev_count = 0
        prev_char = ""

        while max_heap:
            cnt_char, char = heapq.heappop(max_heap)

            if res and res[-1] == char:
                if not max_heap:
                    return ""
                cnt_next, next_char = heapq.heappop(max_heap)
                res.append(next_char)
                cnt_next += 1

                if cnt_next < 0:
                    heapq.heappush(max_heap, (cnt_next, next_char))
                heapq.heappush(max_heap, (cnt_char, char))

            else:
                res.append(char)
                cnt_char += 1
                
                if cnt_char < 0:
                    heapq.heappush(max_heap, (cnt_char, char))

        return "".join(res)
