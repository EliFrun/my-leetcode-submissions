class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1') - (1 if s[0] == '1' else 0)
        zeroes = 0 if s[0] == '1' else 1
        ret = ones + zeroes
        for c in s[1:-1]:
            if c == '0':
                zeroes += 1
            else:
                ones -= 1
            ret = max(ret, zeroes + ones)

        return ret
        
        
