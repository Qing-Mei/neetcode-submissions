class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        res = []

        l, r = 0, n

        while l < r:
            m = (l + r) // 2

            if intervals[m][1] < newInterval[0]:
                l = m + 1
            else:
                r = m
        
        i = 0

        for i in range(l):
            res.append(intervals[i])

        i = l

        start, end = newInterval

        while i < n and end >= intervals[i][0]:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        res.append([start, end])
        
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res
