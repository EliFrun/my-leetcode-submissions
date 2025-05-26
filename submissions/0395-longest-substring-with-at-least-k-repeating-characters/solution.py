class Solution:
    def longestSubstring(self, st: str, l: int) -> int:
        @cache
        def solve(s):
            if len(s) < l:
                return 0
            idxs = defaultdict(list)
            ret = 0
            for i in range(len(s)):
                idxs[s[i]].append(i)
            for k, v in idxs.items():
                if len(v) < l:
                    ret = solve(s[:v[0]])
                    for i in range(len(v) - 1):
                        ret = max(ret, solve(s[v[i] + 1: v[i + 1]]))
                    ret = max(ret, solve(s[v[-1] + 1:]))
                    return ret
            return len(s)  

        return solve(st)
        
        
