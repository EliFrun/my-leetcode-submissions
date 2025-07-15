class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c = Counter(word)
        ret = 0
        for j in range(ord('a'), ord('z') + 1):
            cc = chr(j)
            if c[cc.upper()] > 0 and c[cc] > 0:
                ret += 1
        return ret
