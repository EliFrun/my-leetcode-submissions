class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        M = 1_000_000_007
        @cache
        def solve(rem, idx):
            if rem < 0:
                return 0
            if rem == 0:
                return 1
            if idx >= len(types):
                return 0
            ret = 0
            cnt, marks = types[idx]
            for i in range(cnt + 1):
                if rem - marks * i < 0:
                    break
                ret += solve(rem - marks * i, idx + 1)
            return ret % M

        return solve(target, 0)
        
