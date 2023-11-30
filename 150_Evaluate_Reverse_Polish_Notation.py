class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == '*':
                a, b = stack.pop(), stack.pop()
                stack.append(b * a)
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack.pop()




test = Solution()

tokens = ["2","1","+","3","*"]
print(test.evalRPN(tokens))