class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        found = False
        for i, v in enumerate(s):
            if v == '1':
                if found:
                    if s[i - 1] != '1':
                        return False
                else:
                    found = True
                    
        return True
            
            
         
