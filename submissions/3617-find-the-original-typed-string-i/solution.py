class Solution:
    def possibleStringCount(self, word: str) -> int:
        curr = ''
        word = word + ' '
        cnt = 1
        ret = 1
        second = 0
        for c in word:
            if c == curr:
                cnt += 1
            else:
                ret += cnt - 1
                curr = c
                cnt = 1

        return ret
        
