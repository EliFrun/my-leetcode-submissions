class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n / 3 > limit:
            return 0
        
        ret = 0
        for i in range(max(0, n - 2 * limit), min(n, limit) + 1):
            ret += 1 + min(n - i, limit) - max(n - i - limit, 0)
        return ret
