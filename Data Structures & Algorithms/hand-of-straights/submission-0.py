class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False

        max_num = max(hand)
        freq = [0] * (max_num + 1)

        for num in hand:
            freq[num] += 1

        for start in range(len(freq)):
            while freq[start] > 0:
                for num in range(start, start + groupSize):
                    if num >= len(freq) or freq[num] == 0:
                        return False
                    freq[num] -= 1
        
        return True
