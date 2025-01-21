class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        def pattern(row):
            curr = row[0]
            count = 1
            ret = ''
            for v in row:
                if v != curr:
                    ret += str(count)
                    count = 0
                    curr = v
                count += 1

            ret += str(count)
            return ret

        matrix = [pattern(r) for r in matrix]
        counts = Counter(matrix)
        return max(counts.values())
        
