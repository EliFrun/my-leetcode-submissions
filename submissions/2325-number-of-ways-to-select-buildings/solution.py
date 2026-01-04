class Solution:
    def numberOfWays(self, s: str) -> int:
        ret = 0
        l0, l1 = 0, 0
        r0, r1 = s.count('0'), s.count('1')
        for c in s:
            if c == '0':
                r0 -= 1
            else:
                r1 -= 1

            
            if c == '0':
                ret += l1 * r1
                l0 += 1
            else:
                ret += l0 * r0
                l1 += 1

        return ret
        
