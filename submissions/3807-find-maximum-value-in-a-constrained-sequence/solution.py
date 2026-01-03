class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        ret = [1e9 for _ in range(n)]
        ret[0] = 0
        for idx, v in restrictions:
            ret[idx] = v
        

        for i, v in enumerate(diff):
            ret[i + 1] = min(ret[i] + v, ret[i + 1])

        for i,v in reversed(list(enumerate(diff))):
            ret[i] = min(ret[i + 1] + v, ret[i])

        return max(ret)
        
