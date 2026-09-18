class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        start, end = intervals[0]

        res = []

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]

            if curr_start <= end:
                end = max(curr_end, end)
            else:
                res.append([start, end])
                start, end = curr_start, curr_end
                
        res.append([start, end])
        
        return res
