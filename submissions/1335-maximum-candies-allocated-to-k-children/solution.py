class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def solve(m):
            return sum([c // m for c in candies])

            
        low, high = 1, max(candies)
        while high - low > 1:
            middle = (low + high) // 2
            
            total = solve(middle)
            if total < k:
                high = middle
            else:
                low = middle

        if solve(high) >= k:
            return high
        elif solve(low) >= k:
            return low
        return 0

        
        
