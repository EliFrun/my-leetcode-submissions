class Solution:
    def freqAlphabets(self, s: str) -> str:
        foo = []
        while s:
            if len(s) >= 3 and s[2] == "#":
                foo.append(s[0:2])
                s = s[3:]
            else:
                foo.append(s[0])
                s = s[1:]
                
        return "".join(map(lambda x:chr(96 + int(x)), foo))
            
