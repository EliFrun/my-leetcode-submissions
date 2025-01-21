class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top_sum = [0] * (len(grid[0])  + 1)
        bottom_sum = [0] * (len(grid[0]) + 1)
        for i, v in enumerate(grid[0]):
            top_sum[i] = top_sum[i - 1] + v

        for i, v in enumerate(grid[1][::-1]):
            bottom_sum[-i  - 1] = bottom_sum[-i] + v

        top_sum = top_sum[:-1]
        bottom_sum = bottom_sum[1:]

        m = max(bottom_sum[0] - bottom_sum[0], top_sum[-1] - top_sum[0])
        for i in range(len(top_sum)):
            m = min(m, max(bottom_sum[0] - bottom_sum[i], top_sum[-1] - top_sum[i]))

        return m


        
