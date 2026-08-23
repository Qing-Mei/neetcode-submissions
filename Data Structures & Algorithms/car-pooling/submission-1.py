class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        l, r = float("inf"), float("-inf")

        for trip in trips:
            l = min(l, trip[1])
            r = max(r, trip[2])
        
        n = r - l + 1
        diff = [0] * n

        for passenger, start, end in trips:
            diff[start - l] += passenger
            diff[end - l] -= passenger
        
        curr = 0
        for change in diff:
            curr += change
            if curr > capacity:
                return False
        
        return True
        