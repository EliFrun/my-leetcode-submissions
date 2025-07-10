class Solution:
    def makeFancyString(self, s: str) -> str:
        s += ' '
        curr = ''
        count = 0
        ret = ''
        for c in s:
            if curr == c:
                count += 1
            else:
                ret += curr * min(2, count)
                curr = c
                count = 1

        return ret
