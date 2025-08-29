class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        ret = 0
        for i in range(1, n + 1):
            if i & 1 == 0:
                ret += m & 1
            ret += m // 2
        return ret
