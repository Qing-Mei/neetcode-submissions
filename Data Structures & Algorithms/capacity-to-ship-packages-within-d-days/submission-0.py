class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            curr_weight = 0
            day = 1

            for w in weights:
                if curr_weight + w > capacity:
                    day += 1
                    curr_weight = w
                else:
                    curr_weight += w
                
                if day > days:
                    return False
            
            return True

        l, r = max(weights), sum(weights)

        while l < r:
            m = (l + r) // 2

            if can_ship(m):
                r = m
            else:
                l = m + 1
        
        return l
