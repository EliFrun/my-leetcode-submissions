class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        prefix = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
        ret = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                left = 0 if j - 1 < 0 else prefix[i][j - 1][0]
                above = 0 if i - 1 < 0 else prefix[i - 1][j][1]
                left_diag = 0 if i - 1 < 0 or j - 1 < 0 else prefix[i - 1][j - 1][2]
                right_diag = 0 if i - 1 < 0 or j + 1 >= len(grid[0]) else prefix[i - 1][j + 1][3]
                v = grid[i][j]
                prefix[i][j] = [v + left, v + above, v + left_diag, v + right_diag]

                for k in range(min(i, j), ret - 1, - 1):
                    target = prefix[i][j][0] - (prefix[i][j - k - 1][0] if j - k - 1 >= 0 else 0)
                    
                    diag1 = prefix[i][j][2] - (prefix[i - k - 1][j - k - 1][2] if i - k - 1 >= 0 and j - k - 1 >= 0 else 0)
                    if diag1 != target:
                        continue
                    diag2 = prefix[i][j - k][3] - (prefix[i - k - 1][j + 1][3] if i - k - 1 >= 0 and j + 1 < len(grid[0]) else 0)
                    if diag2 != target:
                        continue
                    if not all(
                        prefix[i][jj][1] - (prefix[i - k - 1][jj][1] if i - k - 1 >= 0 else 0) == target for jj in range(j - k, j + 1)):
                        continue
                    if not all(prefix[ii][j][0] - (prefix[ii][j - k - 1][0] if j - k - 1 >= 0 else 0) == target for ii in range(i - k, i + 1)):
                        continue
                    ret = max(ret, k + 1)
                    break

        return ret


