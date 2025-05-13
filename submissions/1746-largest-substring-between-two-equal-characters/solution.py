class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        idxs = {}
        ret = -1
        for i,c in enumerate(s):
            if c in idxs:
                ret = max(i - idxs[c] - 1, ret)
            else:
                idxs[c] = i

        return ret
