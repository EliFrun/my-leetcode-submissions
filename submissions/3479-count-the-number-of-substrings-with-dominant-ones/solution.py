class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        zeroes = [-1]
        ones = 0
        ret = 0
        for i, c in enumerate(s):
            if c == '0':
                zeroes.append(i)
            else:
                ones += 1
            
            cnt = i - zeroes[-1]
            ret += cnt
            z = 1
            prev = zeroes[-1]
            idx = len(zeroes) - 2
            #print(zeroes)
            while idx >= 0 and z ** 2 <= ones:
                needed = max(0, z ** 2 - cnt)
                diff = prev - zeroes[idx]
                ret += max(0, diff - needed)
                cnt += diff - 1
                prev = zeroes[idx]
                idx -= 1
                z += 1
            #print(c, ret)
        return ret
        


