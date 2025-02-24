class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def solve(i):
            if i >= len(days):
                return 0
            lis_week = [idx for idx, day in enumerate(days) if day >= days[i] + 7]
            lis_month = [idx for idx, day in enumerate(days) if day >= days[i] + 30]
            return min(
                costs[0] + solve(i + 1),
                costs[1] + solve(lis_week[0] if lis_week else len(days)),
                costs[2] + solve(lis_month[0] if lis_month else len(days))
            )

        return solve(0)
        
