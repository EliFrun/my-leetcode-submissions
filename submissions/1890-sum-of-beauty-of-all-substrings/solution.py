class Solution:
    def beautySum(self, s: str) -> int:
        def count(st):
            l = [0] * 26
            for c in st:
                l[ord(c) - ord('a')] += 1
            return l
        cc = [count(s[:i]) for i in range(len(s) + 1)]
        def solve(d1, d2):
            # d1 < d2
            d3 = {}
            for i, v in enumerate(d2):
                if v - d1[i] > 0:
                    d3[i] = v - d1[i]

            return max(d3.values()) - min(d3.values())
        ret = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                v = solve(cc[i], cc[j])
                ret += v
        return ret

        
