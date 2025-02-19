class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        k = k - 1
        def solve(rem, c, opts):
            if c < 0:
                return ''
            print(rem, c, opts)
            ret = opts[int(rem//2**c)]
            ret += solve(rem % 2 ** c, c - 1, 'abc'.replace(ret, ''))
            return ret
        if k >= 3 * 2 ** (n - 1):
            return ''
        ret = 'abc'[k // 2 ** (n - 1)] 
        return ret + solve(k % 2 ** (n - 1), n - 2, 'abc'.replace(ret, ''))
        
