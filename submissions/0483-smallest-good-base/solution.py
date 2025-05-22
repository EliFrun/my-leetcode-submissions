class Solution:
    def smallestGoodBase(self, n: str) -> str:
        def solve(i, k):
            return (k ** (i + 1) - 1) // (k - 1)
        n = int(n)
        for i in range(60, 1, -1):
            left, right = 2, n
            ret = -1
            while left <= right:
                middle = (left + right) // 2
                if solve(i, middle) > n:
                    right = middle - 1
                else:
                    ret = middle
                    left = middle + 1
            if n == solve(i, ret):
                return str(ret)

        return str(n - 1)
