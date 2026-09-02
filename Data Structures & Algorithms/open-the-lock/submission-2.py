class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0

        visited = set(deadends)

        if "0000" in visited:
            return -1

        q1 = set(["0000"])
        q2 = set([target])
        steps = 0

        while q1 and q2:
            if len(q1) > len(q2):
                q1, q2 = q2, q1

            steps += 1
            q3 = set()

            for curr in q1:
                for i in range(4):
                    digit = int(curr[i])

                    for next_digit in [(digit + 1) % 10, (digit - 1) % 10]:
                        nxt = curr[:i] + str(next_digit) + curr[i+1:]

                        if nxt in q2:
                            return steps

                        if nxt not in visited:
                            q3.add(nxt)
                            visited.add(nxt)

            q1 = q3
        
        return -1
