class Solution:
    def longestAwesome(self, s: str) -> int:
        ret = 0
        encodings = {}
        counts = 0
        for i, c in enumerate(s):
            if counts not in encodings:
                encodings[counts] = i
            counts ^= 1 << int(c)
            for j in range(-1, 10):
                com = counts
                if j >= 0:
                    com = counts ^ (1 << j)
                if com in encodings:
                    ret = max(ret, i - encodings[com] + 1)
        return ret
            

        
