class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for passenger, start, end in trips:
            events.append((start, passenger))
            events.append((end, -passenger))
        
        events.sort()
        curr = 0

        for _, passenger in events:
            curr += passenger
            if curr > capacity:
                return False
        
        return True
