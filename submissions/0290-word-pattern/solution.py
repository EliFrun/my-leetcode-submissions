class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def solve(lis):
            l = {}
            curr = 0
            ret = []
            for w in lis:
                if w in l:
                    ret.append(l[w])
                else:
                    l[w] = curr
                    curr += 1
                    ret.append(l[w])

            return ret

        lis_a = solve(list(pattern))
        lis_b = solve(s.split(' '))
        if len(lis_a) != len(lis_b):
            return False
        for a,b in zip(lis_a, lis_b):
            if a != b:
                return False

        return True
