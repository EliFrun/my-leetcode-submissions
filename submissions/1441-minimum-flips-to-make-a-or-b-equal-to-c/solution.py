class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = bin(a)[2:]
        b = bin(b)[2:]
        c = bin(c)[2:]
        
        
        foo = max(len(a), len(b), len(c))
        a = '0' * (foo - len(a)) + a
        b = '0' * (foo - len(b)) + b
        c = '0' * (foo - len(c)) + c
        
        ret = 0
        for i, j, k in zip(a, b, c):
            if k == "1":
                ret += 0 if i == "1" or j == "1" else 1
            if k == '0':
                if i == "1" and j == "1":
                    ret += 2
                elif not (i == "0" and j == "0"):
                    ret += 1
        
        return ret
