class Solution:
    def appealSum(self, s: str) -> int:
        d = defaultdict(int)
        ret = 0
        for i,v in enumerate(s):
            d[v] = i
            for idx in d.values():
                ret += idx + 1
            

        return ret

        
