class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        d = defaultdict(int)
        for x,y in points:
            d[y] += 1
        
        s = 0
        ret = 0
        for k,v in d.items():
            ret = (ret + s * (v * (v - 1)//2)) % 1_000_000_007
            s += (v * (v - 1) // 2)
        return ret

