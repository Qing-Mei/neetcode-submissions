from bisect import bisect_left

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        ordered = sorted((time, idx) for idx, time in enumerate(queries))
        values = [time for time, _ in ordered]

        res = [-1] * n
        parent = list(range(n + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        intervals.sort(key=lambda x: x[1] - x[0])

        for start, end in intervals:
            pos = find(bisect_left(values, start))

            while pos < n and values[pos] <= end:
                original_idx = ordered[pos][1]
                res[original_idx] = end - start + 1

                parent[pos] = find(pos + 1)
                pos = parent[pos]

        return res
        