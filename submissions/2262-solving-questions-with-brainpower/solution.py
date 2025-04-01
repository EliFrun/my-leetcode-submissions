class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def solve(i):
            if i >= len(questions):
                return 0
            p, b = questions[i]
            return max(p + solve(i + b + 1), solve(i + 1))
        return solve(0)
        
