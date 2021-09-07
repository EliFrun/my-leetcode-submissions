class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        a =  min([x for x,y in ops])
        b =  min([y for x,y in ops])
        return a * b
