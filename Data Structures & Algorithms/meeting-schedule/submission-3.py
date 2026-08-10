"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        timeline = [0] * 1000001

        for interval in intervals:
            for i in range(interval.start, interval.end):
                timeline[i] += 1

                if timeline[i] > 1:
                    return False
        
        return True
