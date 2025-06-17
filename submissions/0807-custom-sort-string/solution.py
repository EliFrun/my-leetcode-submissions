class Solution:
    def customSortString(self, order: str, s: str) -> str:
        m = {}
        for i,c in enumerate(order):
            if c not in m:
                m[c] = i
        s = sorted(list(s), key=lambda x: m[x] if x in m else 100)
        return ''.join(s)
        
