class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
            


        
