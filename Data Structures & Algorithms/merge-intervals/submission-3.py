class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[1])

        n = len(intervals)

        start, end = intervals[-1]
        res = []
        for i in range(n - 2, -1, -1):
            curr_start, curr_end = intervals[i]
            if curr_end >= start:
                start = min(start, curr_start)
            else:
                res.append([start, end])
                start, end = curr_start, curr_end
        
        res.append([start, end])

        return res
        