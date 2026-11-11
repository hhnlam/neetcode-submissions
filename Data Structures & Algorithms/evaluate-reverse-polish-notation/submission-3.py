class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {
            '+': lambda a,b:a+b,
            '-': lambda a,b:a-b,
            '*': lambda a,b:a*b,
            '/': lambda a,b:a/b
        }

        for token in tokens:
            if token in operator:
                b = stack.pop()
                a = stack.pop()
                current = operator[token](a,b)
                stack.append(int(current))
            else: stack.append(int(token))
        return int(stack[-1])