class Solution:
    def numberOfWays(self, corridor: str) -> int:
        s_count = corridor.count('S')

        if s_count < 2 or s_count & 1:
            return 0

        cnt = 0
        width = 0
        ret = 1
        for c in corridor:
            if c == 'S':
                cnt += 1
            if cnt == 2:
                width += 1
            if cnt == 3:
                cnt = 1
                ret = (ret * width) % 1_000_000_007
                width = 0
        
        return ret

