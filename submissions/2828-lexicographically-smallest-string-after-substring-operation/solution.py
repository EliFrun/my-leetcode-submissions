class Solution:
    def smallestString(self, s: str) -> str:
        start, end = -1, len(s)
        for i, c in enumerate(s):
            if c == 'a':
                if start >= 0:
                    end = i
                    break
            else:
                if start == -1:
                    start = i

        print(start, end)
        
        s = list(s)
        if start == -1:
            start = -1
            end = 0
        for i in range(start, end):
            s[i] = chr(ord('a') + (ord(s[i]) - 1 - ord('a')) % 26)

        return ''.join(s)
        
