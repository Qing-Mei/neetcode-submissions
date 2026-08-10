from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        
        for num in nums:
            freq[num] += 1
        
        return [num for num, cnt in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]]
