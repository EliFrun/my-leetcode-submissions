class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ret = 0
        curr = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) == 1:
                curr += 1
                ret = max(curr, ret)
                if ret == 26:
                    break
            else:
                curr = 1

        return max(ret, curr)


        
