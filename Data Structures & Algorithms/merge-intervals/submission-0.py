class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        start, end = intervals[0]
        res = []

        for curr_start, curr_end in intervals[1:]:
            if curr_start <= end:
                end = max(end, curr_end)
            else:
                res.append([start, end])
                start, end = curr_start, curr_end
        
        res.append([start, end])

        return res
