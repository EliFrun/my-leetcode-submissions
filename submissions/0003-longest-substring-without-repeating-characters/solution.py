class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr  = set()
        left = 0
        ret = 0
        for c in s:
            while c in curr:
                curr.remove(s[left])
                left += 1
            curr.add(c)
            ret = max(ret, len(curr))
        return ret
            
        
