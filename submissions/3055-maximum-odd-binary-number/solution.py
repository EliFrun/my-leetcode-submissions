class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        o, e = s.count('1'), s.count('0')
        o -= 1
        return '1' * o + '0' * e + '1'
        
