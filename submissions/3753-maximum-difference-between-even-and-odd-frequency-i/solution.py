class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        o = sorted([x for x in c.values() if x & 1])
        e = sorted([x for x in c.values() if not x & 1])
        return o[-1] - e[0]
