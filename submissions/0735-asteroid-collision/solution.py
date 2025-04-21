class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if i > 0:
                stack.append(i)
            if i < 0:
                if stack and stack[-1] > 0:
                    while stack and 0 < stack[-1] < -i:
                        stack.pop(len(stack) - 1)
                    
                    if stack and stack[-1] == -i:
                        stack.pop(len(stack) - 1)
                    elif stack and stack[-1] > -i:
                        continue
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
                        
        return stack
