class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
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
        
