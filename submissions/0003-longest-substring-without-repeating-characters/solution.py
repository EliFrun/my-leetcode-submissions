class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = defaultdict(int)
        left = 0
        ret = 0
        for i,ch in enumerate(s):
            c[ch] += 1
            while any(x > 1 for x in c.values()):
                c[s[left]] -= 1
                left += 1
              
            ret = max(ret, i - left + 1)

        return ret

            
