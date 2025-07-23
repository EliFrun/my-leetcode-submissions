class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        d = defaultdict(lambda: 1)
        day = 1
        for task in tasks:
            day = max(d[task], day)
            d[task] = day + space + 1
            day += 1

        return day - 1

