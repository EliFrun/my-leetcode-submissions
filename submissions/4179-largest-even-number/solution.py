class Solution:
    def largestEven(self, s: str) -> str:
        while s and s[-1] == '1':
            s = s[:len(s) - 1]
        return s
        
