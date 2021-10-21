class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [[s[0], 1]]
        for ch in s[1:]:
            if stack and ch == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop(len(stack) - 1)
            else:
                stack.append([ch, 1])
                
        return "".join([x[0]*x[1] for x in stack])
                
        
