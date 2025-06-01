class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        @cache
        def solve(diff, i):
            if diff < 0:
                return -float('inf')
            if diff == 0:
                return 0
            if i >= len(rods):
                return -float('inf')
            return max(
                solve(diff, i + 1),
                rods[i] + solve(max(-1, diff - 2 * rods[i]), i + 1),
                solve(max(-1, diff - rods[i]), i + 1)
            )

        return solve(sum(rods), 0)
        
