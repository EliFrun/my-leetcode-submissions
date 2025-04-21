class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h = 0
        ret = float("-inf")
        for g in gain:
            ret = max(h, ret)
            h += g

        return max(ret, h)
        
