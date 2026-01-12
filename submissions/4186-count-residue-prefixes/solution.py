class Solution:
    def residuePrefixes(self, s: str) -> int:
        cnt = set()
        ret = 0
        for i,c in enumerate(s):
            cnt.add(c)
            if len(cnt) == (i + 1) % 3:
                ret += 1
        return ret
