class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in match:
                if stack and stack[-1] == match[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return len(stack) == 0
