class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @functools.cache
        def solve(s1, s2):
            if len(s1) == len(s2):
                for i in range(len(s1)):
                    if s1[i] != s2[i]:
                        return 1 + min(
                            solve(s2[i] + s1[i:], s2[i:]),
                            solve(s1[i] + s2[i:], s1[i:]),
                            solve(s2[i] + s1[i + 1:], s2[i:]),
                            solve(s1[i] + s2[i + 1:], s1[i:]),
                            solve(s2[i:], s1[i + 1:]),
                            solve(s1[i:], s2[i + 1:])
                        )
                return 0

            # looking to remove or replace but never add
            if len(s1) > len(s2):
                for i in range(len(s2)):
                    if s1[i] != s2[i]:
                        return 1 + min(solve(s2[i] + s1[i:], s2[i:]), solve(s2[i] + s1[i + 1:], s2[i:]), solve(s1[i + 1:], s2[i:]))

                # means s1[:len(s2)] == s2
                return len(s1) - len(s2)

        shorter = word1 if len(word1) < len(word2) else word2
        longer = word2 if len(word1) < len(word2) else word1
        return solve(longer, shorter)




            
        
