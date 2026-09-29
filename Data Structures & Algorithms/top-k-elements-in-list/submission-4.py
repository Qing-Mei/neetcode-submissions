class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        OFFSET = 1000
        freq = [0] * (OFFSET + 1000 + 1)

        max_freq = 0
        for num in nums:
            freq[num + OFFSET] += 1
            max_freq = max(max_freq, freq[num + OFFSET])
        
        bucket = [[] for _ in range(max_freq + 1)]
        for i, f in enumerate(freq):
            if f > 0:
                bucket[f].append(i - OFFSET)
        
        res = []
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res
