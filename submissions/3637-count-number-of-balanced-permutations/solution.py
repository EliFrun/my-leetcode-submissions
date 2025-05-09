class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        target = sum([int(x) for x in num])
        if target & 1:
            return 0
        
        target //= 2
        if target == 0:
            return 1
        num_s = [num.count(str(i)) for i in range(10)]
        max_count = len(num) // 2 + (len(num) & 1)
        
        @cache
        def solve(s, i, c):
            if c > max_count:
                return 0
            if s == target:
                if len(num) & 1 and c not in [max_count, max_count - 1]:
                    return 0
                if len(num) % 2 == 0 and c != max_count:
                    return 0
                ret = factorial(c) * factorial(len(num) - c)
                for v in num_s[i:]:
                    ret //= factorial(v)
                return ret
            if i > 9:
                return 0

            ret = 0
            for j in range(num_s[i] + 1):
                if s + j * i > target:
                    break
                ret += solve(s + j * i, i + 1, c + j) // (factorial(j) * factorial(num_s[i] - j))
            return ret
            

        return int((solve(0, 0, 0) // (2 if len(num) & 1 else 1))) % 1_000_000_007
        
