class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1],)

        prev_end = intervals[0][1]
        cnt = 0

        for start, end in intervals[1:]:
            if start < prev_end:
                cnt += 1
            else:
                prev_end = end
        
        return cnt
