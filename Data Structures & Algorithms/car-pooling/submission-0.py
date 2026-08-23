import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        min_heap = []

        trips.sort(key=lambda x: x[1])

        curr = 0

        for passenger, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                _, leaving = heapq.heappop(min_heap)
                curr -= leaving
            
            curr += passenger

            if curr > capacity:
                return False

            heapq.heappush(min_heap, (end, passenger))

        return True
