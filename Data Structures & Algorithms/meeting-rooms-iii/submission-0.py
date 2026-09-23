import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = list(range(n))
        cnt = [0] * n
        holding = []

        meetings.sort()

        for start, end in meetings:
            while holding and holding[0][0] <= start:
                _, room = heapq.heappop(holding)
                heapq.heappush(rooms, room)
            
            if rooms:
                room = heapq.heappop(rooms)
                finish = end
            else:
                available_time, room = heapq.heappop(holding)
                finish = available_time + (end - start)
            
            heapq.heappush(holding, (finish, room))
            cnt[room] += 1
        
        return cnt.index(max(cnt))
