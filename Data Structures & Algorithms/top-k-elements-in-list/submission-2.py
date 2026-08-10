class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        offset = 1000

        freq = [0] * (offset + 1000 + 1)

        res = []

        for num in nums:
            freq[num + offset] += 1
        

        cnt = [[] for _ in range((len(nums) + 1))]

        for i, num_freq in enumerate(freq):
            if num_freq > 0:
                cnt[num_freq].append(i - offset)
        
        for num_freq in range(len(cnt) - 1, -1, -1):
            for num in cnt[num_freq]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res
