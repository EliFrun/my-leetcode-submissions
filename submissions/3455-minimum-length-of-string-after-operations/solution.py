class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        ret = 0
        for k,v in c.items():
            if v & 1 == 1:
                ret += 1
            else:
                ret += 2

        return ret
