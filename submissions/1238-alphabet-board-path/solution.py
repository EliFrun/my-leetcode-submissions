class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        alpha = {
            'a': (0,0),
            'b': (0,1),
            'c': (0,2),
            'd': (0,3),
            'e': (0,4),
            'f': (1,0),
            'g': (1,1),
            'h': (1,2),
            'i': (1,3),
            'j': (1,4),
            'k': (2,0),
            'l': (2,1),
            'm': (2,2),
            'n': (2,3),
            'o': (2,4),
            'p': (3,0),
            'q': (3,1),
            'r': (3,2),
            's': (3,3),
            't': (3,4),
            'u': (4,0),
            'v': (4,1),
            'w': (4,2),
            'x': (4,3),
            'y': (4,4),
            'z': (5,0)
        }
        
        curr = alpha['a']
        ret = ""
        for c in target:
            c = alpha[c]
            if curr == (5, 0):
                ret += 'U' * (curr[0] - c[0])
                ret += "R" * (c[1]- curr[1])
                ret += "!"
                curr = c
            elif c == (5, 0):
                ret += "L" * (curr[1]- c[1])
                ret += 'D' * (c[0] - curr[0])
                ret += "!"
                curr = c
            else:
                vert = curr[0] - c[0]
                hor = curr[1] - c[1]
                if vert > 0:
                    ret += "U" * vert
                else:
                    ret += "D" * (-vert)
                if hor > 0:
                    ret += "L" * (hor)
                else:
                    ret += "R" * (-hor)
                    
                ret += "!"
                curr = c
                
        return ret
                
                
