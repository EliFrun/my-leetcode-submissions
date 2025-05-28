class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        c = Counter([(k + x) % k for x in arr])
        for key in c.keys():
            if key == 0 and c[key] & 1:
                return False
            if (c[key] - c[(k - key) % k]) != 0:
                return False

        return True
        
