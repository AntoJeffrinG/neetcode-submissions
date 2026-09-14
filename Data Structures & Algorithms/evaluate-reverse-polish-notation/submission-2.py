class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch not in "+-*/":
                stack.append(int(ch))
            elif ch == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif ch == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif ch == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            elif ch == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
        return stack[-1]
        