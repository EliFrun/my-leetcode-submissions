class Solution:
    def sumZero(self, n: int) -> List[int]:
        ret = [0] if n & 1 else []
        for i in range(1, n//2 + 1):
            ret.extend([-i, i])
        return ret
        
