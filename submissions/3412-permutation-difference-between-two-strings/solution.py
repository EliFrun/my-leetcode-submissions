class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s = { c: i for i,c in enumerate(s) }
        t = { c: i for i,c in enumerate(t) }


        return sum([abs(s[i] - t[i]) for i in s.keys()])
        
