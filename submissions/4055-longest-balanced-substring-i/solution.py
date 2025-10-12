class Solution:
    def longestBalanced(self, s: str) -> int:
        ret = 0
        for i in range(len(s)):
            c = defaultdict(int)
            for j in range(i, len(s)):
                c[s[j]] += 1
                if all(v == c[s[j]] for v in c.values()):
                    ret = max(ret, j - i + 1)
        return ret
