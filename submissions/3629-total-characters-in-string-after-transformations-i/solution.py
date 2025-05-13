class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        c = Counter(s)

        @cache
        def solve(left):
            if left < 26:
                return 1
            else:
                return solve(left - 26) + solve(left - 25)
        
        ret = 0
        for k,v in c.items():
            ret += v * solve(t + ord(k) - ord('a'))

        return ret % 1_000_000_007


        
