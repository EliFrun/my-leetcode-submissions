class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        final = stones[-1]
        stones = set(stones)
        @cache
        def solve(i, k):
            if i not in stones:
                return False
            if i == final:
                return True
            if solve(i + k, k) or solve(i + k + 1, k + 1):
                return True
            if k - 1 > 0:
                return solve(i + k - 1, k - 1) 
            return False

        return solve(1, 1)
        
