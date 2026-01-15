class Solution:
    def maximumLength(self, s: str) -> int:
        d = defaultdict(list)
        curr = s[0]
        cnt = 1
        for c in s[1:]:
            if c == curr:
                cnt += 1
            else:
                insort(d[curr], cnt)
                if len(d[curr]) > 3:
                    d[curr].pop(0)
                curr = c
                cnt = 1

        insort(d[curr], cnt)
        if len(d[curr]) > 3:
            d[curr].pop(0)
        
        ret = -1
        for l in d.values():
            if l[-1] > 2:
                ret = max(ret, l[-1] - 2)
            if len(l) >= 2 and l[-1] + l[-2] >= 3:
                ret = max(ret, min(l[-1] - 1, l[-2]))
            if len(l) >= 3:
                v1,v2,v3 = l
                ret = max(ret, v1)
        return ret
