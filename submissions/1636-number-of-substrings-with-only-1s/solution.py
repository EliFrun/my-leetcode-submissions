class Solution:
    def numSub(self, s: str) -> int:
        ret = 0
        cnt = 0
        for c in s:
            if c == '1':
                cnt += 1
            else:
                ret += cnt * (cnt + 1) // 2
                cnt = 0
        ret += cnt * (cnt + 1) // 2
        return ret % 1_000_000_007
        
