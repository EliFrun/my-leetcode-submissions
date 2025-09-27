class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        costs = [0] + costs
        for i in range(1, len(costs)):
            best = float('inf')
            if i >= 3:
                best = min(best, 9 + costs[i - 3])
            if i >= 2:
                best = min(best, 4 + costs[i - 2])
            best = min(best, 1 + costs[i - 1])

            costs[i] += best
        return costs[-1]
        
