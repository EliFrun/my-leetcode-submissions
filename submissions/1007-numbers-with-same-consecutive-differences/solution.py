class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def solve(prev, left):
            if left == 0:
                return ['']
            ret = []
            if prev + k <= 9:
                ret.extend([str(prev + k) + x for x in solve(prev + k, left - 1)])
            if k != 0 and prev - k >= 0:
                ret.extend([str(prev - k) + x for x in solve(prev - k, left - 1)])
            return ret

        x = []
        for i in range(1, 10):
            x.extend([str(i) + x for x in solve(i, n - 1)])
        return [int(y) for y in x if len(y) == n]
        
