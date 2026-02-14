class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = 0
        curr = [poured]
        while row < query_row:
            nxt = [0] * (len(curr) + 1)
            for i in range(len(curr)):
                curr[i] -= 1
                if curr[i] <= 0:
                    continue
                nxt[i] += curr[i] / 2
                nxt[i + 1] += curr[i] / 2

            curr = nxt
            row += 1

        return min(1, curr[query_glass])
        
