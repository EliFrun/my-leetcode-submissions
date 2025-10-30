class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev = target[0]
        ret = target[0]
        for v in target[1:]:
            if v > prev:
                ret += v - prev
            prev = v
        return ret
        
