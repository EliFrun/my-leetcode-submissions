class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d = set(dictionary)
        @cache
        def solve(i):
            if i >= len(s):
                return 0
            ret = len(s) - i
            for j in range(i, len(s) + 1):
                if s[i:j + 1] in d:
                    ret = min(ret, solve(j + 1))
                ret = min(ret, j - i + 1 + solve(j + 1))
            return ret
        return solve(0)

        
