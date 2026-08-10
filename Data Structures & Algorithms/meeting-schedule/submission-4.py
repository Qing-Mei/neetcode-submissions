"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        time = [0] * 1000001

        for interval in intervals:
            time[interval.start] += 1
            time[interval.end] -= 1
        
        cnt = 0

        for change in time:
            cnt += change

            if cnt > 1:
                return False
        
        return True
