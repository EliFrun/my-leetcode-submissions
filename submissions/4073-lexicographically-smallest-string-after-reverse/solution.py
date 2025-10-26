class Solution:
    def lexSmallest(self, s: str) -> str:
        ret = s
        for i in range(len(s)):
            ret = min(ret, s[:i][::-1] + s[i:], s[:i] + s[i:][::-1])
        return ret
