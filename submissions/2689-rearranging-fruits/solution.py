class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        c = Counter(basket1 + basket2)
        for v in c.values():
            if v % 2 != 0:
                return -1

        
        m = min(c.keys())
        
        needs1 = []
        needs2 = []
        for k,v in Counter(basket1).items():
            if c[k] // 2 < v:
                needs2.extend([k] * (v - c[k]//2))

        for k,v in Counter(basket2).items():
            if c[k] // 2 < v:
                needs1.extend([k] *(v - c[k]//2))

        needs1.sort()
        needs2.sort()

        ret = 0
        while needs1:
            if needs1[0] < needs2[0]:
                ret += min(2 * m, needs1.pop(0))
                needs2.pop()
            else:
                ret += min(2 * m, needs2.pop(0))
                needs1.pop()

                    

        return ret




    
