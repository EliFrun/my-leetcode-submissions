class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        vals = list(range(1, n + 1))
        ret = ''
        while vals:
            if k == 0:
                ret += ''.join([str(x) for x in vals])
                break
            idx = (k - 1) // factorial(len(vals) - 1)
            k -= factorial(len(vals) - 1) * idx
            ret += str(vals.pop(idx))
        return ret
        
