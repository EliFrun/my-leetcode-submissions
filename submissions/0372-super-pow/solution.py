class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def mod(num, a):
            res = 0
            for i in range(0, len(num)):
                res = (res * 10 + int(num[i])) % a
            return res

        exponent = mod(b, 1140)
        if exponent == 0:
            exponent = 1140
        ret = 1
        for _ in range(exponent):
            ret = ((a % 1337) * (ret % 1337)) % 1337
        return ret
