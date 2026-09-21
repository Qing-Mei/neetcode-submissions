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
        meeting = []
        cnt = 0

        for interval in intervals:
            start, end = interval.start, interval.end

            if meeting and meeting[0] <= start:
                heapq.heappop(meeting)
            
            heapq.heappush(meeting, end)
    
        return len(meeting)
