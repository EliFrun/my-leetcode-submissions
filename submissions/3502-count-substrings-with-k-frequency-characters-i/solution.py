class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        counts = [0] * 26
        left = 0
        ret = 0
        for i, c in enumerate(s):
            counts[ord(c) - ord('a')] += 1
            while any(x >= k for x in counts):
                ret += len(s) - i
                counts[ord(s[left]) - ord('a')] -= 1
                left += 1
        return ret
