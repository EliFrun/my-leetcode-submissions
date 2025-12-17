class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # best previous, minimum_prev, max_prev
        l = [[0, float('-inf'), float('-inf')] for _ in range(k + 2)]
        for p in prices:
            for i in range(len(l) - 2, -1, -1):
                if l[i][1] < l[i][0] + p:
                    l[i][1] = l[i][0] + p
                if l[i][2] < l[i][0] - p:
                    l[i][2] = l[i][0] - p
                if l[i][0] < l[i - 1][1] - p:
                    l[i][0] = l[i - 1][1] - p
                if l[i][0] < l[i - 1][2] + p:
                    l[i][0] = l[i - 1][2] + p
        ret = 0
        for i in range(len(l) - 2, -1, -1):
            if ret < l[i][0]:
                ret = l[i][0]
                break
        return ret
