class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @cache
        def solve(prev, groups_left, idx):
            if groups_left > len(houses) - idx:
                return float('inf')
            if groups_left < 0:
                return float('inf')
            if idx >= len(houses):
                return 0 if groups_left == 0 else float('inf')

            if houses[idx] != 0:
                if prev != houses[idx]:
                    groups_left -= 1
                return solve(houses[idx], groups_left, idx + 1)
            ret = float('inf')
            for i in range(n):
                res = cost[idx][i] + solve(i + 1, groups_left - (1 if i + 1 != prev else 0), idx + 1)
                ret = min(ret, res)
            return ret

        ret = solve(0,target, 0)
        if ret == float('inf'):
            return -1
        return ret
            
        
