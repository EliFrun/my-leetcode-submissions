class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        @cache
        def options(prev):
            ret = [[]]
            for i in range(m):
                nxt = []
                for l in ret:
                    for j in range(3):
                        if prev[i] == j:
                            continue
                        if l and l[-1] == j:
                            continue
                        nxt.append(l + [j])
                ret = nxt
            return ret

        @cache
        def solve(n_left, prev_column):
            if n_left == 0:
                return 1
            return sum(solve(n_left - 1, tuple(option)) for option in options(prev_column))

        return solve(n, tuple([-1] * m)) % 1_000_000_007

            
        
