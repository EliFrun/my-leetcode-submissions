class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        groups = [x % batchSize for x in groups]
        c = [0] * batchSize
        for group in groups:
            c[group] += 1

        ret = c[0]
        c[0] = 0


        for i in range(1, batchSize//2 + 1):
            m = min(c[i], c[-i])
            if i == batchSize - i:
                ret += m // 2
                c[i] -= (m // 2) * 2
            else:
                ret += m
                c[i] -= m
                c[batchSize - i] -= m
        
        @cache
        def best(l, idx, s):
            if s > 0 and s % batchSize == 0:
                return 1 + best(l, 0, 0)
            
            if sum(l) == 0:
                return 1 if s > 0 else 0

            if idx == len(l):
                return 0
            
            ret = 0
            l = list(l)
            for i in range(l[idx] + 1):
                l[idx] -= i
                ret = max(ret, best(tuple(l), idx + 1, s + idx * i))
                l[idx] += i

            return ret

        ret += best(tuple(c), 0, 0)
        return ret

"""
3
[0, 1, 8, 3, 2, 5, 8]
4
[0, 0, 8, 3, 2, 5, 7]
9
[0, 0, 3, 3, 2, 0, 7]
11
[0, 0, 3, 1, 0, 0, 7]
11
[0, 0, 3, 1, 0, 0, 7]
14
[0, 0, 0, 1, 0, 0, 1]
15
[]
"""

            

        
