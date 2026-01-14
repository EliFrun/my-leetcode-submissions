class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        distinct_x = set()

        for x, l in positions:
            distinct_x.update([x, x + l])

        distinct_x = sorted(list(distinct_x))

        heights = [0] * (len(distinct_x) - 1)
        ret = []
        ma = 0
        for x, l in positions:
            idx_l = bisect_left(distinct_x, x)
            idx_r = bisect_right(distinct_x, x + l) - 1
            m = 0
            for i in range(idx_l, idx_r):
                if heights[i] > m:
                    m = heights[i]

            for i in range(idx_l, idx_r):
                heights[i] = m + l

            ma = max(ma, m + l)
            ret.append(ma)

        return ret
        
