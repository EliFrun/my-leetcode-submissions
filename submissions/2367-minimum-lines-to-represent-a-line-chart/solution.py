class Solution:
    def minimumLines(self, s: List[List[int]]) -> int:
        if len(s) < 2:
            return 0
        
        s.sort()
        ret = 1
        slope = (s[1][1] - s[0][1], s[1][0] - s[0][0])
        for i in range(2, len(s)):
            new_slope = (s[i][1] - s[i - 1][1], s[i][0] - s[i - 1][0])
            if new_slope[0] * slope[1] != new_slope[1] * slope[0]:
                ret += 1
                slope = new_slope
        return ret

        
