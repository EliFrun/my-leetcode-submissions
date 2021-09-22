class Solution:
    def checkRecord(self, s: str) -> bool:
        def foo(a):
            bar = a.split('A')
            for i in bar:
                for j in i.split('P'):
                    if len(j) >= 3:
                        return False
                    
            return True
            
        return s.count('A') < 2 and foo(s)
