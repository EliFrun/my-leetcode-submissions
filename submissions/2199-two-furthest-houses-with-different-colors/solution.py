class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        d = {}
        ret = 0
        for i, c in enumerate(colors):
            if c not in d:
                d[c] = i
            for k in d.keys():
                if k == c:
                    continue
                ret = max(ret, i - d[k])

        return ret

        
