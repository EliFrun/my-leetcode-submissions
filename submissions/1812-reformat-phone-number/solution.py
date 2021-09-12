class Solution:
    def reformatNumber(self, number: str) -> str:
        s = ""
        
        for i in number:
            if i.isnumeric():
                s += i

        return self.foo(s)
                
    def foo(self, s):
        if len(s) == 4:
            return f'{s[:2]}-{s[2:]}'
        if len(s) <= 3:
            return s
        
        return s[0:3] + '-' + self.foo(s[3:])
