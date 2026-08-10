class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in match:
                if not stack:
                    return False

                if stack[-1] != match[ch]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)
        
        return len(stack) == 0
