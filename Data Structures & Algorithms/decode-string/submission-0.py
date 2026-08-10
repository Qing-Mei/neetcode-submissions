class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        curr = ""

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == "[":
                stack.append((curr, num))

                num = 0
                curr = ""

            elif ch == "]":
                prev, repeat = stack.pop()

                curr = prev + curr * repeat

            else:
                curr += ch
        
        return curr
        