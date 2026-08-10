class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(speed):
            hour = 0

            for banana in piles:
                hour += (banana + speed - 1) // speed

                if hour > h:
                    return False

            return True

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
