class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        mixed = [[x,y] for x,y in zip(difficulty, profit)]
        mixed.sort(key=lambda x: (x[0], -x[1]))

        m = mixed[0][1]
        for i in range(len(mixed)):
            if m > mixed[i][1]:
                mixed[i][1] = m
            m = max(m, mixed[i][1])
        
        mixed = sorted(list(set([tuple(x) for x in mixed])))

        def most_profit(diff):
            nonlocal mixed
            l = 0
            u = len(mixed) - 1
            if diff < mixed[0][0]:
                return 0

            while abs(l - u) > 1:
                mid = (l + u) // 2
                if diff < mixed[mid][0]:
                    u = mid
                elif diff > mixed[mid][0]:
                    l = mid
                else:
                    return mixed[mid][1]


            if mixed[u][0] <= diff:
                return mixed[u][1]
            return mixed[l][1]


        return sum([most_profit(diff) for diff in worker])
        
