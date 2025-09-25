class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(
                    triangle[i - 1][max(0, j - 1)],
                    triangle[i - 1][min(len(triangle[i - 1]) - 1, j)]
                )
        
        return min(triangle[-1])

        
