class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        @cache
        def solve(s1, s2):
            if len(s1) == 0 or len(s2) == 0:
                return ''
            
            if s1[0] == s2[0]:
                return s1[0] + solve(s1[1:], s2[1:])
            
            r1 = solve(s1[1:], s2)
            r2 = solve(s1, s2[1:])
            if len(r1) > len(r2):
                return r1
            return r2
            
        lcs = solve(str1, str2)
        #print(lcs)

        ret = []
        i, j = (0, 0)
        for c  in lcs:
            while i < len(str1) and str1[i] != c:
                ret.append(str1[i])
                i += 1
            
            while j < len(str2) and str2[j] != c:
                ret.append(str2[j])
                j += 1
            
            ret.append(c)
            i += 1
            j += 1
        ret.extend(list(str1[i:]))
        ret.extend(list(str2[j:]))

        return ''.join(ret)


        
