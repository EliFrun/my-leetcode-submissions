class Solution:
    def punishmentNumber(self, n: int) -> int:
        def solve(target, num_str):
            if target < 0:
                return False
            if len(num_str) == 0:
                return target == 0
            for i in range(1,len(num_str) + 1):
                if solve(target - int(num_str[:i]), num_str[i:]):
                    return True
            return False

        ret = 0
        for i in range(n + 1):
            if solve(i,str(i * i)):
                ret += i * i

        return ret

        
