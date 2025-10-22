class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        @cache
        def solve(a, b, i):
            if i >= len(costs):
                return 0
            
            if a == 0:
                return costs[i][1] + solve(a, b - 1, i + 1)
            if b == 0:
                return costs[i][0] + solve(a - 1, b, i + 1)
            return min(costs[i][0] + solve(a - 1, b, i + 1), costs[i][1] + solve(a, b - 1, i + 1))  
        return solve(len(costs)//2, len(costs)//2, 0)      
