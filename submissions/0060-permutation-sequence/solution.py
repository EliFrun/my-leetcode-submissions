class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        vals = [str(i) for i in range(1, n + 1)]
        ret = ""
        while n > 0:
            i = k // factorial(n - 1)
            ret += vals[i]
            vals.pop(i)
            k %= factorial(n - 1)
            n -= 1
        return ret
