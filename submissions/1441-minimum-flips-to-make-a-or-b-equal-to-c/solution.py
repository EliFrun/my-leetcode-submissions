class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a, b, c = bin(a)[2:], bin(b)[2:], bin(c)[2:]
        a = '0' * (max(len(a), len(b), len(c)) - len(a)) + a
        b = '0' * (max(len(a), len(b), len(c)) - len(b)) + b
        c = '0' * (max(len(a), len(b), len(c)) - len(c)) + c
        ret = 0
        for x,y,z in zip(a,b,c):
            x,y,z = int(x), int(y), int(z)
            if z == 1:
                if x == 0 and y == 0:
                    ret += 1
            else:
                ret += x + y

        return ret
                    
        
