class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def cnt(v):
            return sum([bisect_right(matrix[i], v) for i in range(len(matrix))])
        lower, upper = matrix[0][0], matrix[-1][-1]

        while lower < upper:
            middle = (lower + upper) // 2
            if cnt(middle) < k:
                lower = middle + 1
            else:
                upper = middle

        return lower        
