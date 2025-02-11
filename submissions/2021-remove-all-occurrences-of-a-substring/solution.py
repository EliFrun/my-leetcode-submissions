class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for c in s:
            if c == part[-1] and len(stack) >= len(part) - 1:
                stack.append(c)
                remove = True
                for i in range(1, len(part) + 1):
                    if stack[-i] != part[-i]:
                        remove = False
                        break
                
                if remove:
                    stack = stack[:len(stack)-len(part)]
            else:
                stack.append(c)

        return ''.join(stack)
