class Solution:
    def buddyStrings(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        def counts(foo):
            a = defaultdict(int)
            for v in foo:
                a[v] += 1
            return a
        
        d1 = counts(s1)
        d2 = counts(s2)
        
        for k in d1.keys():
            if d1[k] != d2[k]:
                return False
            
        if s1 == s2:
            return any(x >= 2 for x in d1.values())
        
        diffs = 0
        a1, a2, b1, b2 = "", "", "", ""
        for i, j in zip(s1, s2):
            if i != j:
                if diffs == 0:
                    a1, a2 = i, j
                elif diffs == 1:
                    b1, b2 = i, j
                else:
                    return False
                diffs += 1
                
        return a1 == b2 and a2 == b1
