class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ret = []
        p = 0
        while n > 0:
            ret.append(int((n % 10) * (10 ** p)))
            n //= 10
            p += 1
        return [x for x in ret[::-1] if x]
