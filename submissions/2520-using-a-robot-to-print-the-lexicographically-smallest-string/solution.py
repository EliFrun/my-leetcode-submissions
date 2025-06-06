class Solution:
    def robotWithString(self, s: str) -> str:
        c = Counter(s)
        s = list(reversed(s))
        t = []
        ret = []
        queue = sorted(list(c.keys()))
        while s:
            curr = queue.pop(0)
            #print(s, t, ret, curr)
            while t and t[-1] <= curr:
                ret.append(t.pop())
            while s and c[curr] > 0:
                v = s.pop()
                if v == curr:
                    ret.append(v)
                else:
                    t.append(v)
                c[v] -= 1
        return ''.join(ret + t[::-1])
