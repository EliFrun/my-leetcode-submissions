class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = set()
        right_c = Counter(s)
        right = set(list(s))

        chars = defaultdict(set)
        for c in s:
            right_c[c] -= 1
            if right_c[c] <= 0:
                right.remove(c)
            chars[c] = chars[c].union(left.intersection(right))
            left.add(c)

        ret = 0
        for c, opts in chars.items():
            ret += len(opts)

        return ret

        
