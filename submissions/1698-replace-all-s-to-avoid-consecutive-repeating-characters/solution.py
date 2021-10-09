class Solution:
    def modifyString(self, s: str) -> str:
        if len(s) < 2:
            return 'a' if s == '?' else s
        s = list(s)
        if s[0] == '?':
            if s[1] == '?':
                s[0] = 'a'
            else:
                s[0] = chr(ord('a') + (ord(s[1]) - 96) % 26)
                
        if s[-1] == '?':
            if s[-2] == '?':
                s[-1] = 'a'
            else:
                s[-1] = chr(ord('a') + (ord(s[-2]) - 96) % 26)
                
        for i in range(1, len(s) - 1):
            if s[i] == '?':
                a, b = s[i - 1], s[i + 1]
                if 'a' not in [a,b]:
                    s[i] = 'a'
                elif 'b' not in [a, b]:
                    s[i] = 'b'
                else:
                    s[i] = 'c'
                    
        return ''.join(s)
