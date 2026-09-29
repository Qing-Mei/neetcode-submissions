class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        order = sorted((value, key) for key, value in freq.items())

        res = []

        for i in range(len(order) - 1, len(order) - 1 - k, -1):
            res.append(order[i][1])
        
        return res

