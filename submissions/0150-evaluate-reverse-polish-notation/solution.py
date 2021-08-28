class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.isnumeric() or i[1:].isnumeric():
                stack.append(i)
            else:
                if i == "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(a) + int(b))
                elif i == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b) - int(a))
                elif i == "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(a) * int(b))
                elif i == "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(int(b) / int(a)))
                    
                    
        return stack[0]
