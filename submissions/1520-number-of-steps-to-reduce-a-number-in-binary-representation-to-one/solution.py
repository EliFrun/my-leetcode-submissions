class Solution:
    def numSteps(self, s: str) -> int:
        ret = 0
        l = list(s[::-1])
        while len(l) > 1:
            if l[0] == '1':
                ret += 1
                i = 0
                while i < len(l) and l[i] == '1':
                    l[i] = '0'
                    i += 1
                if i < len(l):
                    l[i] = '1'
                else:
                    l.append('1')
            else:
                ret += 1
                l.pop(0)

        return ret
