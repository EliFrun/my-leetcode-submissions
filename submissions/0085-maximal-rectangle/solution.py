class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        curr = [0] * len(matrix[0])

        ret = 0
        for row in matrix:
            for i,v in enumerate(row):
                curr[i] = curr[i] + 1 if v == "1" else 0

            stk = [(-1, 0)]
            for i, num in enumerate(curr):
                ret = max(ret, num)
                last_idx = i
                while stk and stk[-1][1] >= num:
                    j,v = stk.pop()
                    last_idx = j
                stk.append((last_idx, num))
                for j,v in stk:
                    ret = max(ret, (v * (i - j + 1)))
        
        return ret

