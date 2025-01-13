class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        for ss in s:
            if t == '':
                break
            if ss == t[0]:
                t = t[1:]

        return len(t)

        
