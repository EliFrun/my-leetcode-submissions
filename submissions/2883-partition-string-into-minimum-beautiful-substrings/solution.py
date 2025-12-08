class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        @cache
        def solve(i):
            if i >= len(s):
                return 0
            if s[i] == '0':
                return float('inf')
            curr = 0
            ret = float('inf')
            for j in range(i, len(s)):
                curr <<= 1
                curr += int(s[j])
                if 5 ** int(log(curr, 5)) == curr:
                    ret = min(ret, 1 + solve(j + 1))
            return ret
        res = solve(0)

        if res != float('inf'):
            return res
        return -1
                
