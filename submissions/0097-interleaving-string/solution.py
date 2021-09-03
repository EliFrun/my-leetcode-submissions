class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        
        a = self.helper(s1,s2,s3,memo)
        return a
    
    
    def helper(self, s1, s2, s3, memo):
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if not s3:
            return not s1 and not s2
        if (len(s1), len(s2)) in memo:
            return memo[(len(s1), len(s2))]
        else:
            if s1[0] == s3[0] and s2[0] == s3[0]:
                a = self.helper(s1[1:], s2, s3[1:], memo)
                memo[(len(s1) - 1, len(s2))] = a
                b = False
                if not a:
                    b = self.helper(s1, s2[1:], s3[1:], memo)
                    memo[(len(s1), len(s2) - 1)] = b
                return a or b
            elif s1[0] == s3[0]:
                a = self.helper(s1[1:], s2, s3[1:], memo)
                memo[(len(s1) - 1, len(s2))] = a
                return a
            elif s2[0] == s3[0]:
                b = self.helper(s1, s2[1:], s3[1:], memo)
                memo[(len(s1), len(s2) - 1)] = b
                return b
            else:
                return False
