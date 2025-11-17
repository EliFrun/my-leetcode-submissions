class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = x // abs(x)
        x = abs(x)
        ret = sign * int(str(x)[::-1])
        if not - 2 ** 31 <= ret <= 2 ** 31 - 1:
            return 0
        return ret
