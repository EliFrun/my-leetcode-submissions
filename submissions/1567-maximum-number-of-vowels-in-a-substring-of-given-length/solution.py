class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left, right = 0,0
        count = 0
        ret = 0
        while right < len(s):
            if right - left >= k:
                count -= (1 if s[left] in 'aeiou' else 0)
                left += 1
            count += (1 if s[right] in 'aeiou' else 0)
            right += 1

            ret = max(ret, count)

        return ret
        
