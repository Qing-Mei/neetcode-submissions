import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        max_heap = []

        for char, count in [("a", a), ("b", b), ("c", c)]:
            if count > 0:
                heapq.heappush(max_heap, (-count, char))
        
        while max_heap:
            cnt_char, char = heapq.heappop(max_heap)

            if len(res) >= 2 and res[-1] == char and char == res[-2]:
                if not max_heap:
                    break
                
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
        