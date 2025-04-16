class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        @cache
        def solve(i, n):
            if i >= len(satisfaction):
                return 0
            return max(n * satisfaction[i] + solve(i + 1, n + 1), solve(i + 1, n))

        return solve(0,1)
                    
