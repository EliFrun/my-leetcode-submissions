class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        h = []
        for i, l in enumerate(values):
            heappush(h, (l.pop(), i))
        i = 1
        ret = 0
        while h:
            v, idx = heappop(h)
            ret += i * v
            i += 1
            if values[idx]:
                heappush(h, (values[idx].pop(), idx))

        return ret
