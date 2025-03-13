class Solution:
    def countTime(self, time: str) -> int:
        ret = 1
        if time[0] == '?':
            if time[1] == '?':
                ret *= 24
            elif int(time[1]) < 4:
                ret *= 3
            else:
                ret *= 2

        elif time[1] == '?':
            if time[0] == '2':
                ret *= 4
            else:
                ret *= 10
        
        if time[3] == '?':
            ret *= 6

        if time[4] == '?':
            ret *= 10

        return ret
