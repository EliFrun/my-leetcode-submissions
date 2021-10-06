class Solution:
    def minTimeToType(self, word: str) -> int:
        curr_pos = 'a'
        ret = 0
        for c in word:
            ret += 1 + min(abs(ord(curr_pos) - ord(c)), 26 - abs(ord(curr_pos) - ord(c)))
            curr_pos = c
            
        return ret
