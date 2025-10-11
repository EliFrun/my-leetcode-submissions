class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        c = Counter(power)
        l = sorted(c.keys())
        @cache
        def solve(i):
            if i >= len(l):
                return 0
            k = l[i]
            j = i + 1
            while j < len(l) and l[j] <= k + 2:
                j += 1
            return max(c[k] * k + solve(j), solve(i + 1))
        return solve(0)

            
