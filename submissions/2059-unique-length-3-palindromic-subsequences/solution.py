class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = set()
        right = Counter(s)
        ret = defaultdict(set)
        for c in s:
            right[c] -= 1
            if right[c] == 0:
                right.pop(c)
            ret[c] |= (left & set(right.keys()))
            left.add(c)
        return sum([len(x) for x in ret.values()])
