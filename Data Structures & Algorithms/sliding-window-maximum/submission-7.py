import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        res = []

        for i, num in enumerate(nums):
            heapq.heappush(max_heap, (-num, i))

            while max_heap and max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            
            if i >= k - 1:
                res.append(-max_heap[0][0])
        
        return res
        