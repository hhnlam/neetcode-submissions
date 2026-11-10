class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        if len(s) < 2: return False

        for c in s:
            if c in valid:
                if stack and stack[-1]==valid[c]:
                    stack.pop(-1)
                else: return False
            else: stack.append(c)
        return not stack