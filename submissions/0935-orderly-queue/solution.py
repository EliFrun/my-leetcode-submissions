class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ret = s
            for i in range(len(s)):
                ret = min(ret, s[i:] + s[:i])
            return ret
        return ''.join(sorted(list(s)))
