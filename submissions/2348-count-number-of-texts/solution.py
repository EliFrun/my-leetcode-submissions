class Solution:
    def countTexts(self, s: str) -> int:
        letters3 = set('234568')
        
        @cache
        def solve(i):
            if i >= len(s):
                return 1
            ret = 0
            for j in range(3 if s[i] in letters3 else 4):
                if i + j >= len(s):
                    break
                if s[i + j] != s[i]:
                    break
                ret = (ret + solve(i + j + 1)) % 1_000_000_007

            return ret
        return solve(0)

            
        
