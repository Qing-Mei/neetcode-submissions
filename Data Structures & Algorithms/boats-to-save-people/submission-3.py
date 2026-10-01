class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        max_weight = max(people)

        freq = [0] * (max_weight + 1)

        for w in people:
            freq[w] += 1

        cnt = 0

        l = 0

        r = len(freq) - 1

        while l <= r:
            while l <= r and freq[l] == 0:
                l += 1
            
            while l <= r and freq[r] == 0:
                r -= 1

            if l > r:
                break

            freq[r] -= 1
            if l + r <= limit and freq[l] > 0:
                freq[l] -= 1

            cnt += 1

        return cnt
