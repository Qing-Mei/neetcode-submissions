import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        min_heap = []

        for num, f in freq.items():
            heapq.heappush(min_heap, (f, num))
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        res = [num for f, num in min_heap]
        
        return res
