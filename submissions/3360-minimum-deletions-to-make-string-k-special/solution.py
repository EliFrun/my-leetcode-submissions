class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        c = Counter(word)
        ll = sorted(c.values())
        
        def solve(l):
            if not l:
                return 0
            best = 0
            for v in l[1:]:
                best += max(0, v - (l[0] + k))
            return min(
                best,
                l[0] + solve(l[1:])
            )

        return solve(ll)
        
