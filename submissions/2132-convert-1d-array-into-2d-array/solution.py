class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        ret = []
        for i in range(m):
            ret.append(original[i * n: (i + 1) * n])
        return ret
