class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a, b = bin(x)[2:], bin(y)[2:]
        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        if len(b) < len(a):
            b = "0" * (len(a) - len(b)) + b
        ret = 0
        for i, j in zip(a, b):
            ret += 1 if i != j else 0
            
        return ret
