class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        h = []
        waiting = []
        for k, v in c.items():
            heappush(h, -v)

        t = 0
        while waiting or h:
            while waiting and waiting[0][0] <= t:
                _, v = heappop(waiting)
                heappush(h, v)

            if h:
                v = heappop(h)
                if v + 1 < 0:
                    heappush(waiting, (t + n + 1, v + 1))
                t += 1
            else:
                t = waiting[0][0]

        return t
        
