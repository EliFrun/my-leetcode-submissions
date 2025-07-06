class Solution:
    def numberOfWays(self, s: str) -> int:
        s = [int(c) for c in s]
        left = [0,0]
        right = [0,0]
        for c in s:
            right[c] += 1

        ret = 0
        for c in s:
            right[c] -= 1
            ret += left[1 - c] * right[1 - c]
            left[c] += 1

        return ret
        

