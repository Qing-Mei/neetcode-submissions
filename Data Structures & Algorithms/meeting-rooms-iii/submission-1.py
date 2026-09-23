import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [(0, room) for room in range(n)]
        heapq.heapify(rooms)
        cnt = [0] * n

        meetings.sort()

        for start, end in meetings:
            while rooms[0][0] < start:
                _, room = heapq.heappop(rooms)
                heapq.heappush(rooms, (start, room))

            available_time, room = heapq.heappop(rooms)

            finish = available_time + (end - start)
            heapq.heappush(rooms, (finish, room))
        
            cnt[room] += 1
        
        return cnt.index(max(cnt))
