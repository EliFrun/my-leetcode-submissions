class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s = Counter(s)
        t = Counter(t)

        ret = 0
        for k in set(s.keys()) | set(t.keys()):
            ret += abs(s.get(k, 0) - t.get(k, 0))

        return ret
        
