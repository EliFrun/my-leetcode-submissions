class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def solve(k):
            return sum(ceil(x/k) for x in piles)

        left, right = 1, 2**31 - 1
        while left < right:
            middle = (left + right) // 2
            if solve(middle) > h:
                left = middle + 1
            elif solve(middle) <= h:
                right = middle



        return left

        
