class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:

        @cache
        def solve(i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            
            v = 0
            ret = 0
            while i < len(s):
                v *= 10
                v += ord(s[i]) - ord('0')
                i += 1
                if v <= k:
                    ret = (ret + solve(i)) % 1_000_000_007
                else:
                    break
            return ret

        return solve(0)
        
