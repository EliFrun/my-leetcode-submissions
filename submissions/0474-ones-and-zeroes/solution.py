class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs = [(s.count('0'), s.count('1')) for s in strs]


        @cache
        def solve(i, mm, nn):
            ret = 0
            if i >= len(strs):
                return 0
            if mm >= strs[i][0] and nn >= strs[i][1]:
                ret = 1 + solve(i + 1, mm - strs[i][0], nn - strs[i][1])
            return max(ret, solve(i + 1, mm, nn))
        return solve(0, m, n)
