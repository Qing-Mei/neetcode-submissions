class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        curr = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            curr += diff

            if curr < 0:
                start = i + 1
                curr = 0
        
        return start if total >= 0 else -1
        