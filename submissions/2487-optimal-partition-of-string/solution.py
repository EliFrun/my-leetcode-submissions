class Solution:
    def partitionString(self, s: str) -> int:
        d = set()
        ret = 1
        for c in s:
            if c in d:
                ret += 1
                d = set()
            d.add(c)

        return ret

        
