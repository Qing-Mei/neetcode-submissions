from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque(senate)

        r_count = senate.count("R")
        d_count = len(senate) - r_count

        r, d = 0, 0

        while r_count > 0 and d_count > 0:
            curr = q.popleft()

            if curr == "R":
                if d > 0:
                    d -= 1
                    r_count -= 1
                else:
                    q.append(curr)
                    r += 1
            else:
                if r > 0:
                    r -= 1
                    d_count -= 1
                else:
                    q.append(curr)
                    d += 1
        
        return "Radiant" if r_count > 0 else "Dire"
