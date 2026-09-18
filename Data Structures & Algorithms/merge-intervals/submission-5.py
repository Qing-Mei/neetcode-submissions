class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        starts = sorted(start for start, end in intervals)
        ends = sorted(end for start, end in intervals)

        res = []
        left = 0
        i = 0
        n = len(intervals)

        while i < n:
            if i == n - 1 or starts[i + 1] > ends[i]:
                res.append([starts[left], ends[i]])
                left = i + 1
            i += 1
        
        return res
