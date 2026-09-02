from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)

        if "0000" in visited:
            return -1

        q = deque(["0000"])
        visited.add("0000")
        steps = 0

        while q:
            sz = len(q)

            for _ in range(sz):
                curr = q.popleft()

                if curr == target:
                    return steps

                for i in range(4):
                    digit = int(curr[i])

                    for next_digit in [(digit + 1) % 10, (digit - 1) % 10]:
                        nxt = curr[:i] + str(next_digit) + curr[i+1:]

                        if nxt not in visited:
                            q.append(nxt)
                            visited.add(nxt)

            steps += 1
        
        return -1
