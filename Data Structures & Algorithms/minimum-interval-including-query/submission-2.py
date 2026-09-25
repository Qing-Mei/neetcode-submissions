from bisect import bisect_left, bisect_right

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        values = sorted(set(queries))
        size = len(values)
        INF = float("inf")

        tree = [INF] * (4 * size)

        def update(node, l, r, ql, qr, length):
            if qr < l or ql > r:
                return
            
            if ql <= l and qr >= r:
                tree[node] = min(tree[node], length)
                return
            
            mid = (l + r) // 2

            update(node * 2, l, mid, ql, qr, length)
            update(node * 2 + 1, mid + 1, r, ql, qr, length)
        
        for start, end in intervals:
            left = bisect_left(values, start)
            right = bisect_right(values, end) - 1

            if left <= right:
                update(1, 0, size - 1, left, right, end - start + 1)
            
        ans = [-1] * size

        def collect(node, l, r, best):
            best = min(best, tree[node])

            if l == r:
                ans[l] = best if best != INF else -1
                return
            
            mid = (l + r) // 2
            collect(node * 2, l, mid, best)
            collect(node * 2 + 1, mid + 1, r, best)
        
        collect(1, 0, size - 1, INF)

        lookup = dict(zip(values, ans))
        return [lookup[q] for q in queries]

