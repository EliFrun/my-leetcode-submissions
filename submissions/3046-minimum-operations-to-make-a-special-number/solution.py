class Solution:
    def minimumOperations(self, num: str) -> int:
        num = list(num[::-1])
        
        @cache
        def solve(i, prev):
            if i >= len(num):
                return float('inf') if prev != '0' else 0
            if prev == '0' and num[i] in ('0', '5'):
                return 0
            elif prev == '5' and num[i] in ('2', '7'):
                return 0
            elif prev:
                return 1 + solve(i + 1, prev)
            ret = 1 + solve(i + 1, None)
            if num[i] in ('0', '5'):
                ret = min(ret, solve(i + 1, num[i]))
            return ret

        return min(solve(0, None), len(num))


        
