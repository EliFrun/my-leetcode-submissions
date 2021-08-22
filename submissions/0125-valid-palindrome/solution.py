class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.strip()
        s = s.lower()
        
        s = ''.join([x for x in s if x.islower() or x.isnumeric()])
        
        
        return s == s[::-1]
        
