class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for a in asteroids:
            while stk and stk[-1] > 0 and stk[-1] < -a:
                stk.pop()
            if a > 0:
                stk.append(a)
            elif stk and a == -stk[-1]:
                stk.pop()
                continue
            elif not stk or stk[-1] < 0:
                stk.append(a)
        return stk

        
