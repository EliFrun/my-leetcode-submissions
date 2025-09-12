class Solution:
    def doesAliceWin(self, s: str) -> bool:
        cnt = 0
        st = set('aeiou')
        for c in s:
            if c in st:
                return True
        return False
        
