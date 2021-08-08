class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ['{', '(', '[']
        right = ['}', ')', ']']
        for c in s:
            if c in left:
                stack.append(c)

            if c in right:
                if stack and left.index(stack[-1]) == right.index(c):
                    stack.pop()
                else:
                    return False
                
        return True if not len(stack) else False
