class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        max_weight = max(stones)
        buckets = [0] * (max_weight + 1)

        for stone in stones:
            buckets[stone] += 1

        first = max_weight
        second = max_weight - 1

        while first > 0:
            buckets[first] %= 2

            if buckets[first] == 0:
                first = second
                second -= 1
                continue

            second = min(second, first - 1)

            while second > 0 and buckets[second] == 0:
                second -= 1

            if second == 0:
                return first

            buckets[first] = 0
            buckets[second] -= 1

            diff = first - second
            buckets[diff] += 1

            if diff > second:
                first = diff
            else:
                first = second
                second -= 1
        
        return 0
