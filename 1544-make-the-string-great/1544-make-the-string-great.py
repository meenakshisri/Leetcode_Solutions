class Solution:
    def makeGood(self, s: str) -> str:

        stack = []

        for ch in s:
            if not stack or (abs(ord(stack[-1])-ord(ch)) != 32):
                stack.append(ch)            
            else:
                stack.pop()
        
        return "".join(stack)


        
        