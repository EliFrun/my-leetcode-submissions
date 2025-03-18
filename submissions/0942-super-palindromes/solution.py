class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def super_palindromes_between(l, r):
            l = int(sqrt(int(l)))
            r = int(sqrt(int(r)))
            ret = []
            for i in range(10_000):
                for k in ([str(x) for x in range(10)] + ['']):
                    if i == 0:
                        if k:
                            a = int(k)
                        else:
                            continue
                    else:
                        a = int(str(i) + k + str(i)[::-1])    
                    if a >= l and a <= r:
                        ret.append(a)
            return ret

        r = []
        for p in super_palindromes_between(left, right):
            sq = str(p * p)
            if sq == sq[::-1]:
                r.append(sq)

        return len(r)
