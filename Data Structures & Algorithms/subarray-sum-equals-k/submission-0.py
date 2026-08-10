from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        
        freq[0] = 1
        curr = 0        
        cnt = 0

        for num in nums:
            curr += num
            need = curr - k
            cnt += freq[need]
            freq[curr] += 1
        
        return cnt
