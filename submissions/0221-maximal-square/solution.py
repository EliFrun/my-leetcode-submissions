class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def solve(heights):
            heights.append(0)
            stack = [-1]
            ret = 0
            for i, v in enumerate(heights):
                while v < heights[stack[-1]]:
                    curr = stack.pop()
                    height = heights[curr]
                    if i - stack[-1] - 1 >= height:
                        ret = max(ret, height)
                stack.append(i)

            return ret
        
        curr = [int(x) for x in matrix[0]]
        ret = solve(curr)
        for i in range(1, len(matrix)):
            curr = [x + int(y) if int(y) > 0 else 0 for x,y in zip(curr, matrix[i])]
            ret = max(solve(curr), ret)

        return ret * ret
        
