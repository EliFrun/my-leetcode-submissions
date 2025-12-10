class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        m = complexity[0]
        ret = 1
        for i in range(1, len(complexity)):
            if complexity[i] <= m:
                return 0
            ret = (ret * i) % 1_000_000_007
        return ret
