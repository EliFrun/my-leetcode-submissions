class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        lis = [[0] * x for x in range(1, 101)]
        lis[0][0] = poured
        for i in range(99):
            if all([x == 0 for x in lis[i]]):
                break
            for j in range(len(lis[i])):
                to_lose = max(0, lis[i][j] - 1)
                lis[i][j] -= to_lose
                lis[i + 1][j] += to_lose / 2
                lis[i + 1][j + 1] += to_lose / 2

        return min(1, lis[query_row][query_glass])
        
        
