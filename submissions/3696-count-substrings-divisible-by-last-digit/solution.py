class Solution:
    def countSubstrings(self, s: str) -> int:
        ret = 0
        mods = [[]]
        for v in range(1, 10):
            mods.append([0] * v)

        for c in s:
            c = int(c)
            for i in range(1, 10):
                next_mod = [0] * i
                for j in range(i):
                    next_mod[(10 * j + c) % i] += mods[i][j]
                next_mod[c % i] += 1
                mods[i] = next_mod
            
            if c != 0:
                ret += mods[c][0]

        return ret
        
