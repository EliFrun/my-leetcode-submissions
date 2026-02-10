class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        curr = 0
        a = 0
        b = 0
        c = 0
        d = 0
        for i in range(n):
            curr |= 1 << i
            a |= 1 << i
            if i % 2 == 0:
                b |= 1 << i
            if i % 2 == 1:
                c |= 1 << i
            if i % 3 == 0:
                d |= 1 << i


        curr = set([curr])
        for _ in range(presses):
            nxt = set()
            for s in curr:
                nxt.add(s ^ a)
                nxt.add(s ^ b)
                nxt.add(s ^ c)
                nxt.add(s ^ d)

            curr = nxt
        return len(curr)
                
                

        
