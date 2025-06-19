class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def solve_2(v1, v2):
            ret = [v1 + v2, v1 - v2, v1 * v2]
            if v2 != 0:
                ret.append(v1/v2)
            return ret

        def solve_3(v1, v2, v3):
            ret = []
            for v in solve_2(v2, v3):
                ret.append(v1 + v)
                ret.append(v1 - v)
                ret.append(v1 * v)
                if v != 0:
                    ret.append(v1/v)

            for v in solve_2(v1, v2):
                ret.append(v + v3)
                ret.append(v - v3)
                ret.append(v * v3)
                if v3 != 0:
                    ret.append(v/v3)

            return ret 

        def solve_4(v1,v2,v3,v4):
            ret = []
            for a in solve_2(v1, v2):
                for b in solve_2(v3, v4):
                    ret.append(a + b)
                    ret.append(a - b)
                    ret.append(a * b)
                    if b != 0:
                        ret.append(a / b)

            for v in solve_3(v1,v2,v3):
                ret.append(v + v4)
                ret.append(v - v4)
                ret.append(v * v4)
                if v4 != 0:
                    ret.append(v / v4)

            for v in solve_3(v2,v3,v4):
                ret.append(v1 + v)
                ret.append(v1 - v)
                ret.append(v1 * v)
                if v != 0:
                    ret.append(v1 / v)
            
            return ret
        
        for v1, v2, v3, v4 in permutations(cards):
            if any([abs(x - 24) < 0.000001 for x in solve_4(v1,v2,v3,v4)]):
                return True
        return False


        
