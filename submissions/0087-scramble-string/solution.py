class Solution:
    def isScramble(self, st1: str, st2: str) -> bool:
        @functools.cache
        def solve(s1, s2):
            if len(s1) == 1:
                return s1 == s2
            if s1 == s2:
                return True
            if sorted(s1) != sorted(s2):
                return False

            return any(
                [ 
                    (
                        solve(s1[:i], s2[:i]) and solve(s1[i:], s2[i:]) or
                        solve(s1[:i], s2[-i:]) and solve(s1[i:], s2[:-i])
                    )
                    for i in range(1, len(s1))
                ]
            )

        return solve(st1, st2)

        
