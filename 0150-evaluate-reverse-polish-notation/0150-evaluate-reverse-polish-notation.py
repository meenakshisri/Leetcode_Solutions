class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for token in tokens:
            if token in ['+','-','*','/']:
                x = stack.pop()
                y = stack.pop()
                if token == '+':
                    stack.append(x+y)
                elif token == '-':
                    stack.append(y-x)
                elif token == '*':
                    stack.append(x*y)
                else: 
                    stack.append(int(y/x))  # Don't use floor division, instead use int , as it should truncate towardszero for both +ve and -ve values       
            else:
                stack.append(int(token))

        return stack[-1]




        