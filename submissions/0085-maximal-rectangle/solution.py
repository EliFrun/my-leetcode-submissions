class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
    
        def solve(heights):
            heights.append(0)
            stack = [-1]
            ret = 0
            for i, v in enumerate(heights):
                while v < heights[stack[-1]]:
                    curr = stack.pop()
                    height = heights[curr]
                    ret = max(ret, height * (i - stack[-1] - 1))
                stack.append(i)

            return ret

        curr = matrix[0]
        m = 0
        i = 0
        while i < len(matrix):
            m = max(m, solve(curr))
            if i + 1 >= len(matrix):
                break
            curr = [x + y if y == 1 else 0 for x,y in zip(curr, matrix[i + 1])]
            i += 1

        return m
