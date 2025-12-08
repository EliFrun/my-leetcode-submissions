class Solution:
    def countTriples(self, n: int) -> int:
        ret = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                v = i ** 2 + j ** 2
                if sqrt(v) == int(sqrt(v)) and sqrt(v) <= n:
                    ret += 2
        return ret
