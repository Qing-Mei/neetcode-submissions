import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        meetings = []
        cnt = 0

        for interval in intervals:
            start, end = interval.start, interval.end

            while meetings and meetings[0] <= start:
                heapq.heappop(meetings)
            
            heapq.heappush(meetings, end)

            cnt = max(cnt, len(meetings))
        
        return cnt
